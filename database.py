from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://o54qlx45dtcqpvb20w9a:pscale_pw_j6Ixk75QuGAesoRTbQ5eQXo4x4zydxq3vWksrk9kdso@aws.connect.psdb.cloud/kyivdb?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_cert": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from places"))
  
column_names = result.keys()
    
result_dicts = []
    
for row in result.all():
  result_dicts.append(dict(zip(column_names, row)))
print(result_dicts)

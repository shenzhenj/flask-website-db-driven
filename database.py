from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://83wcywhjmad8d0lt9pxz:pscale_pw_YtMv41lvVGbS7rGQpwrgWM4MrOYTxjNTLN0GDI5NVp@aws.connect.psdb.cloud/kyivdb?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_cert": "/etc/ssl/cert.pem"
                       }})

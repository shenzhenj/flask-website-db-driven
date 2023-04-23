from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_places_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from places"))
  column_names = result.keys()
  result_dicts = []
  for row in result.all():
    result_dicts.append(dict(zip(column_names, row)))
  return result_dicts

@app.route("/")
def hello_kyiv():
  places = load_places_from_db()
  return render_template("home.html", places=places)

@app.route("/places")
def list_places():
  places_json = load_places_from_db()
  return jsonify(places_json)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

from flask import Flask, render_template, jsonify

app = Flask(__name__)

PLACES = [{
  "id": 1,
  "title": "Khreschatyk",
  "meaning": "Heart of Kyiv"
}, {
  "id": 2,
  "title": "Kyiv-Pechersk Lavra",
  "meaning": "Soul of Kyiv"
}, {
  "id": 3,
  "title": "Hidropark",
  "meaning": "Health of Kyiv"
}]


@app.route("/")
def hello_kyiv():
  return render_template("home.html", places=PLACES)

@app.route("/places")
def list_places():
  return jsonify(PLACES)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

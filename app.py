from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/add", methods=["GET","POST"])
def done():
    return "meow"


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

import firebasehandler

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("page.html", title="HOME PAGE")

@app.route("/docs")
def docs():
    return render_template("page.html", title="docs page")

@app.route("/about")
def about():
    return render_template("page.html", title="about page")

if __name__ == "__main__":
    app.run(debug=True)
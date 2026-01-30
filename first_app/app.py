from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("initialpage.html")

@app.route("/about")
def about_me():
    return render_template("aboutme.html")

if __name__ == "__main__":
    app.run(debug=True)


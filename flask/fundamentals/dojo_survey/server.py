from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/results", methods = ["POST"])
def results():
    print(request.form)
    return render_template("results.html", name = request.form['name'], locations = request.form['locations'],languages = request.form['languages'])


if __name__== "__main__":
    app.run(debug = True)
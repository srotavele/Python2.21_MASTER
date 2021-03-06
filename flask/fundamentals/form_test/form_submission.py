from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['usermail'] = request.form['email']
    print(request.form)
    return redirect("/show")

@app.route('/show')
def show():
    print("Showing User Info from Form")
    print(request.form)
    return render_template("show.html", name_on_template=session['username'], email_on_template=session['usermail'])


if __name__=='__main__':
  app.run(debug=True)
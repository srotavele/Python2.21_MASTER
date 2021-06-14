from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "nunyaBizness"


@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        count = session['count'] = 1
        print(request.form)
    return render_template('index.html')

@app.route('/visits', methods = ['POST'])
def add_visits():
    print(request.form)
    session['count'] +=2
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def destroy_session():
    print(request.form)
    session.clear()
    return redirect('/')





if __name__ =="__main__":
    app.run(debug = True)
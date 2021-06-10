from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html', phrase= "hello",times =5)

@app.route('/play')
def play_boxes():
    return render_template('index.html', phrase= "hello",times =5)

@app.route('/dojo')
def dojo():
    return "Dojo"
    
@app.route('/hello/<name>')
def say_name(name):
    print(name)
    return (f"Hi, {name} !!")

@app.errorhandler(404)
def not_found(bug):
    return f"Sorry, pal. Page Not Found. Try Again"
    
@app.route('/repeat/<int:number>/<greeting>')
def repeat(number, greeting):
    print(greeting)
    return (f" {greeting} ") * number

if __name__=="__main__":
    app.run(debug=True)
    
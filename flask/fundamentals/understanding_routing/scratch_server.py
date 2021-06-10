from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!!'

@app.route('/dojo')
def dojo():
    return "Dojo"
    
@app.route('/hello/<name>')
def say_name(name):
    print(name)
    return "Hi " + name + "!!"
    
@app.route('/repeat/<int:number>/<greeting>')
def repeat(number, greeting):
    print(greeting)
    return greeting * number
if __name__=="__main__":
    app.run(debug=True)
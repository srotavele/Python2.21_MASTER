from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/<x>')
def base_rows(x):
    return render_template('index.html', height = 8, width = int(x))

@app.route('/<x>/<y>')
def base_rows(x,y):
    return render_template('index.html', height = int(x), width = int(y))


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def base_user(x,y, color1, color2):
    return render_template('index.html',height = int(x), width  = int(y), color1 = , color2 =)



if __name__=="__main__":
    app.run(debug = True)
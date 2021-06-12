from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html', x = 8, y = 8, color_1 = "black", color_2 = "red")

@app.route('/<int:x>')
def base_row1(x):
    return render_template('index.html', x = x, y = 8, color_1 = "black", color_2 = "red")

@app.route('/<int:x>/<int:y>')
def base_row2(x,y):
    return render_template('index.html', x = x, y = y, color_1 = "black", color_2 = "red" )


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def base_user(x,y, color1, color2):
    return render_template('index.html',x = x, y = y, color_1 = color1 , color_2 = color2)

if __name__=="__main__":
    app.run(debug = True)
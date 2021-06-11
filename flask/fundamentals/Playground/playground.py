from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/')
def blue_boxes(num = 3, color = "blue"):
    return render_template('index.html_2',num = 3, color = "blue")

@app.route('/play/<int:num>')
def num_boxes(num):
    return render_template('index_2.html', times = num)

# @app.route('/play/<int:num>/<color>')
# def color_boxes(num, color):
    return render_template('index_2.html', times = num, color = color )
    
if __name__=="__main__":
    app.run(debug=True)

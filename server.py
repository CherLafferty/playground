from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello/<string:name>/<int:num>')
def hello(name,num):
    return render_template("hello.html",name=name,num=num)

@app.route('/play')
def play():
    return render_template("play.html",num=3,color="blue")

@app.route('/play/<int:num>')
def play_num(num):
    return render_template("play.html",num=num,color="blue")

@app.route('/play/<int:num>/<string:color>')
def color(num,color):
    return render_template("play.html",num=num,color=color)

if __name__ == "__main__":
    app.run(debug = True)
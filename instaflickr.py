
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('block.html', name=name)

if __name__ == "__main__":
    app.run()

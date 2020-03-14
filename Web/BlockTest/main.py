from flask import Flask, render_template
from CotentManager import Names
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', Names = Names())

if __name__ == '__main__':
    app.run(debug=True)
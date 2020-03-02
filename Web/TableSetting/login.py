from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def login():
    return render_template('tablelayout.html',number = 10)
    pass


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True);
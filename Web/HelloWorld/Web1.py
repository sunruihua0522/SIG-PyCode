from flask import Flask, Request

app =Flask(__name__)

@app.route('/')
def HelloWold():
    return 'Hello World'

@app.route('/login/')
def Login():
    return 'Login......'


@app.route('/login/<int:id>/')
def LoginWithVar(id):
    return '<h1>Welcome %d to my world !</h1>'%id

@app.route("/foo/<string:username>/")
def foo(username):
    return "loginSteing %s"%username

app.run(host ='0.0.0.0', port = 8080)


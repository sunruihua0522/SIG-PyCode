from flask import Flask,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def foo():
    return 'Hello world'

@app.route('/user/',methods=['POST','GET'])
def login():
    if (request.method == 'GET'):
        return 'Welcom %s from python and flask' % (request.args.get('nm'))
    else:
        return 'Welcom %s from python and flask' % (request.form['nm'])


# if(__name__ == '__main__'):
#     app.run(host='0.0.0.0',port = 5000, debug=True)
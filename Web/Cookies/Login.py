from flask import Flask,Response,make_response,request,render_template

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def login():
    if(request.method == 'POST'):
        name = request.form['Name']
        resp = make_response(render_template('ReadCookie.html'))
        resp.set_cookie('USERID',name)
        resp.set_cookie('AGE','29')
        resp.set_cookie('Address','USA')
        resp.set_cookie('Score','100')
        return resp

@app.route('/Read/', methods=['POST','GET'])
def ReadCK():
    name = request.cookies.get('USERID')
    res = ''
    for k,v in request.cookies.items():
        res += '<br>%s = %s </br>'%(k,v)
    return '获取到了cookie就是 %s' % res

@app.route('/ReadAgain/', methods=['POST','GET'])
def ReadCKAgain():
    name = request.cookies.get('USERID')
    res = ''
    for k,v in request.cookies.items():
        res += '<br>%s = %s </br>'%(k,v)
    return '获取到了cookie就是 %s' % res


if __name__ == '__main__':
    app.run(port = 8080)
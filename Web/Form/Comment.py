from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def GetInfo():
    dic = {}
    l = {'Name','Physics','Chemistry','Mathematics'}
    if(request.method == 'POST'):
        for k in l:
            dic.update({k :request.form[k]})
        # dic ={'a':55,'b':77}
        return render_template('info.html',infos = dic)
    else:
        for k in l:
            dic.update({k :request.args.get(k)})
        # dic = {'a': 55, 'b': 77}
        return render_template('info.html', infos=dic)


if __name__ == '__main__':
    app.run(port = 8080)
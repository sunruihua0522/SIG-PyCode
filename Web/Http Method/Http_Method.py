from flask import Flask,request,url_for,redirect
app = Flask(__name__)



@app.route('/success/<name>/')
def success(name):
    return 'Welcome %s' % name

@app.route('/login/',methods=['POST','GET'])
def login():
    if(request.method == 'POST'):
        user = 'Get from post data: %s'%(request.form['nm'])
        return redirect(url_for('success',name = user))
    else:
        user = 'Get from get:%s' % request.args.get('nm')
        return redirect(url_for('success', name = user))

if __name__=='__main__':
    app.run(port=8080)
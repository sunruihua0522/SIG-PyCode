from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/index/<string:user>/')
def Index(user):
    return render_template('1.html',name = user)



@app.route('/getList/', methods=['GET','POST'])
def Result():
    dict = {'Jacey':23, 'Lucy':55, 'LinTao':'WuHan'}
    return render_template('Result.html', result = dict)


if __name__ == '__main__':
    app.run(port = 8080)
from flask import Flask, render_template,url_for,request, redirect
app = Flask(__name__)

@app.route('/index/')
def index ():
    pass


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        usr = request.form['nm']
        # return redirect(url_for('loginok', usr=usr))
        return render_template('loginok.html', usr=usr)
    else:
        return render_template('login.html')

@app.route('/loginok/<string:usr>')
def loginok(usr):
    return render_template('loginok.html',usr = usr)

if __name__ == '__main__':
    app.run(debug=True)
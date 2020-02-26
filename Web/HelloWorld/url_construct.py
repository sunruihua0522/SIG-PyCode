from flask import Flask,request,url_for,redirect

app = Flask('URL构建')

@app.route('/admin/')
def HelloAdmin():
    return 'Hello Admin'

@app.route('/guest/<guestname>')
def HelloGuest(guestname):
    return 'Hello %s as Guest'%guestname

@app.route('/user/<string:name>/')
def HelloUser(name):
    if(name == 'admin'):
        return redirect(url_for(('HelloAdmin')))
    else:
        return redirect(url_for('HelloGuest',guestname = name))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)
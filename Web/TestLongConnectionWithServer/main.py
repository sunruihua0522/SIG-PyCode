from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template
import datetime,time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('client.html')

@app.route('/api')
def api():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        orgin =  ws.origin
        print('%s加入连接'%orgin)
        while True:
            message = ws.receive()
            for _ in range(int(message)):
                time.sleep(0.5)
                msg = '%s:  %s'%(datetime.datetime.now().__str__(), message)
                ws.send(msg)

    return

if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1',5000), application= app, handler_class=WebSocketHandler)
    http_server.serve_forever()
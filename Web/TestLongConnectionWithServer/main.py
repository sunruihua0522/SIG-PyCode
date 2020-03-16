from flask import Flask,request,render_template
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket

app = Flask(__name__)

app.route('/',methods=['POST','GET'])
def index():
    client_socket = request.environ.get('wsgi.websocket')

    while True:
        #msg = client_socket.recive()

        msg = client_socket.receive()
        client_socket.send(msg + 'from web service')

@app.route('/chart')
def chart():
    return render_template('client.html')
if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1',8888),application=app,
                             handler_class=WebSocketHandler)
    http_server.serve_forever()


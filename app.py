from flask import Flask
from flask_socketio import SocketIO, emit
from random import randint

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return open('html/index.html').read()

@socketio.on('log')
def logMessage(msg):
    print(f' * Log: {msg["data"]}')
    emit('log',msg)

@socket.on('setData')
def setData(data):
    emit('updateChartData', data, broadcast=True)


if __name__ == '__main__':

    #app.run('127.0.0.1',3000)
    socketio.run(app, '127.0.0.1',3000)

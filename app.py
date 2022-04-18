from flask import Flask
from flask_socketio import SocketIO,send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myScrect'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handlemessage(msg):
    print(f"Message {msg}")
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)

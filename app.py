
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# Handle signaling for WebRTC
@socketio.on('signal')
def handle_signal(data):
    # Broadcast the signaling data to all clients except the sender
    emit('signal', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000, debug=True)


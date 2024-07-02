from flask_socketio import SocketIO, emit

socketio = SocketIO(cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('message', {'data': 'Connected'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    emit('response', {'data': 'Message received'})

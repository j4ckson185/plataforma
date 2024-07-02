from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, messaging
from websocket import socketio

# Configurações do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Inicialização do Firebase Admin SDK
cred = credentials.Certificate("C:\\xampp\\plataforma motoboys\\Delivery\\motoboys-a41e6-firebase-adminsdk-dr0g8-084b1f32d6.json")
firebase_admin.initialize_app(cred)

# Rota para criar pedidos
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    token = data.get('token')
    order_id = data.get('order_id')
    # Enviar notificação via Firebase Cloud Messaging
    message = messaging.Message(
        notification=messaging.Notification(
            title='New Order',
            body=f'Order {order_id} has been created!'
        ),
        token=token
    )
    response = messaging.send(message)
    return jsonify(success=True), 201

# Inicialização do SocketIO
socketio.init_app(app)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5005, debug=True)

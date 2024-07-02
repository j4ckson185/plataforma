from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, messaging
from websocket import socketio
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Inicialização do Firebase Admin SDK
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL")
})
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

import firebase_admin
from firebase_admin import credentials, messaging

# Verificar se o app Firebase já foi inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate("C:/xampp/plataforma motoboys/Delivery/motoboys-a41e6-firebase-adminsdk-dr0g8-084b1f32d6.json")
    firebase_admin.initialize_app(cred)

def send_push_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=token
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)

import paho.mqtt.client as mqtt
import time
from definitions.definitions_client1 import cliente_id, user, password, server, port

# Seta o topico deste cliente
topic = 'pucpr/iot/chat/' + cliente_id + '/'

# funcao responsavel por seta as mesg


def get_message(client, user, msg):
    if(msg.topic != topic):
        print("\n[Bob] => " + msg.payload.decode())
        send_message(cliente_id)


def send_message(client_id):
    mensage = input('[' + client_id + '] => ')
    # print(mensage)
    if(mensage != None or mensage != ''):
        client.publish(topic, mensage)


# Realiza conexão com broker
client = mqtt.Client(cliente_id)
client.username_pw_set(user, password)
client.connect(server, port)

# Verifica se recebeu mesg
client.on_message = get_message
client.subscribe('pucpr/iot/chat/#')
client.loop_start()
mensage = ''

while(True):
    send_message(cliente_id)

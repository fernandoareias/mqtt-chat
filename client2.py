import paho.mqtt.client as mqtt
import time
from definitions.definitions_client2 import cliente_id, user, password, server, port

# Seta o topico deste cliente
topic = 'pucpr/iot/chat/' + cliente_id + '/'

# funcao responsavel por seta as mesg


def get_message(client, user, msg):
    if(msg.topic != topic):
        print("\n[Fernando] => " + msg.payload.decode())
        send_message()


def send_message():
    msg = ''
    msg = input('[' + cliente_id + '] => ')
    if(mensage != None and mensage != ''):
        client.publish(topic, mensage)
        print('\r\n')


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
    print('\n')
    send_message()

import paho.mqtt.client as mqtt

host = 'broker.emqx.io'
port = 8883

topics = dict(apmt='fanta/apmt')


def on_connect(self, client, userdata, rc):
    print('MQTT Connected.')
    self.subscribe(topics['apmt'])


def on_message(client, userdata, msg):
    print(msg.payload.decode('utf-8', 'strict'))


def connectMQTT():
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host)
    client.loop_start()


def publish(topic, payload):
    client.publish(topic, payload)

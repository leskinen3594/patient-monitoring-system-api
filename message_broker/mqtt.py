import json
import paho.mqtt.client as mqtt
import time

host = 'broker.emqx.io'
port = 8883

topics = dict(apmt='fanta/apmt', log='fanta/log')


def on_connect(self, client, userdata, rc):
    print('MQTT Connected.')
    self.subscribe(topics['apmt'])
    self.subscribe(topics['log'])


def on_message(client, userdata, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8', 'strict')

    match topic:
        case 'fanta/apmt':
            print('getting an appointment ...')
            time.sleep(3)
            publish('fanta/apmt/machine', '{"pt_id":"xxx","dr_id":"xxx"}')
        case 'fanta/log':
            json_string = json.loads(message)
            print(json_string)


def connectMQTT():
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host)
    client.loop_start()

    return client


def publish(topic, payload):
    client.publish(topic, payload)
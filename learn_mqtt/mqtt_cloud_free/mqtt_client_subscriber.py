import paho.mqtt.client as mqtt
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Subscriber")
client.connect(mqttBroker)

def on_message(client, userdata, message):
    print("Recieved message: ", str(message.payload.decode("utf-8")))

client.loop_start()
client.subscribe("mqtt_practice_topic")
client.on_message = on_message
time.sleep(30)
client.loop_stop()

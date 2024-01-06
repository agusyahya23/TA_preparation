import paho.mqtt.client as mqtt
from kafka_producer import Producer
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Subscriber")
client.connect(mqttBroker)

producer = Producer()

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    print("Recieved MQTT message: ", data )
    print("Sending message to Kafka topic: ", data )
    producer.produce_data(data)

client.loop_start()
client.subscribe("mqtt_kafka_topic")
client.on_message = on_message
time.sleep(1000)
client.loop_stop()

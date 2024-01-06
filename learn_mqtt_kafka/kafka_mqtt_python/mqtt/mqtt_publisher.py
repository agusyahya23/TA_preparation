import paho.mqtt.client as mqtt
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Publisher")
client.connect(mqttBroker)

while True:
    user_input = input("Entered something: ")
    client.publish("mqtt_kafka_topic", user_input)
    print("MQTT published: ", user_input)
    time.sleep(1)
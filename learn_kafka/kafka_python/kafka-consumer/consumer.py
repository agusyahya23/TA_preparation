from json import loads
from kafka import KafkaConsumer

class Consumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            'hello_world',
            value_deserializer=lambda x: loads(x),
            group_id='hello_group',
            auto_offset_reset='latest'
        )
        
    def consume_data(self):
        for message in self.consumer:
            print("Received message: ", message.value)
            return message.value
        
    

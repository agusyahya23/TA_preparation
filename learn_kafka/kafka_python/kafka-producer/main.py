import time
import os
from producer import Producer

producer = Producer()

def produce_message():
    user_input = input("Enter something: ")
    
    print("You entered:", user_input)
    
    producer.produce_data(user_input)
    
while True:
    produce_message()
    time.sleep(5)

    
    

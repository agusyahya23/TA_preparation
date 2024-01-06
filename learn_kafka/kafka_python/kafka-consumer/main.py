from consumer import Consumer

consumer = Consumer()

def get_data():
    try:
        data = consumer.consume_data()
        return data
    except ValueError:
        return "error"
    
while True:
    get_data()
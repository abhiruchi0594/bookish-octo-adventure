import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (it will only be created if it doesn't exist)
channel.queue_declare(queue='hello')

# Publish a message to the queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello from Service A!'.encode())

print(" [x] Sent 'Hello from Service A!'")

connection.close()

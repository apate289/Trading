import pika
import json
import time, os


# RabbitMQ connection settings
rabbitmq_host = 'localhost'
queue_name = 'test_queue_2'
user = os.getenv('RABBITMQ_USER', 'guest')
password = os.getenv('RABBITMQ_PASSWORD', 'guest')
host = os.getenv('RABBITMQ_HOST', 'localhost')
port = int(os.getenv('RABBITMQ_PORT', 5672))


def callback(ch, method, properties, body):
    message_data = json.loads(body)
    message_content = message_data.get('message')
    print(f" [x] Received {message_content}")
    #time.sleep(1)  # Simulate processing time
    ch.basic_ack(delivery_tag=method.delivery_tag)

credentials = pika.PlainCredentials(user, password)
parameters = pika.ConnectionParameters(host=host, 
                                        port=port, 
                                        credentials=credentials)
#self.connection = pika.BlockingConnection(parameters)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue=queue_name, durable=True)

#channel.basic_qos(prefetch_count=10)
if not channel:
    raise Exception("Connection is not established.")
channel.basic_consume(queue=queue_name, on_message_callback=callback,auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
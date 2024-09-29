import pika
import json

def send_task_creation_message(task_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_creation_queue', durable=True)

    # Send the message to RabbitMQ
    channel.basic_publish(
        exchange='',
        routing_key='task_creation_queue',
        body=json.dumps(task_data),
        properties=pika.BasicProperties(delivery_mode=2)  # Make message persistent
    )
    connection.close()
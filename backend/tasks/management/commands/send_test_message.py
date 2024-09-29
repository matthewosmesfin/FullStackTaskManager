import json
import pika
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Send a test message to RabbitMQ'

    def handle(self, *args, **kwargs):
        # Create a test message
        print("Command Loaded")
        test_task = {
            'title': 'Test Task',
            'description': 'This is a test task.',
            'completed': False,
            'user': f'http://localhost:8000/users/1/'
        }

        # Establish connection to RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='task_creation_queue', durable=True)

        # Publish the test message
        channel.basic_publish(
            exchange='',
            routing_key='task_creation_queue',
            body=json.dumps(test_task),
            properties=pika.BasicProperties(delivery_mode=2)  # Make message persistent
        )

        print(" [x] Sent 'Test Task'")
        connection.close()

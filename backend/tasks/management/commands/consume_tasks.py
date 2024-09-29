import os
import django
import pika
import json
from django.core.management.base import BaseCommand
from tasks.models import Task
from tasks.serializers import TaskSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Consume messages from RabbitMQ and create tasks.'

    def handle(self, *args, **kwargs):
        # Initialize Django settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
        django.setup()

        def process_task(ch, method, properties, body):
            print("Received a message from RabbitMQ")  # Added print for debugging
            task_data = json.loads(body)
            print(f"Task data: {task_data}")  # Print the task data for debugging

            serializer = TaskSerializer(data=task_data)
            if serializer.is_valid():
                print("Creating task...")  # Added print for debugging
                serializer.save()
                self.stdout.write(self.style.SUCCESS(f"Task '{task_data['title']}' created for user ID {task_data['user']}"))
            else:
                print("Validation failed")  # Added print for debugging
                self.stdout.write(self.style.ERROR(f"Failed to create task: {serializer.errors}"))

            ch.basic_ack(delivery_tag=method.delivery_tag)

        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='task_creation_queue', durable=True)

            channel.basic_consume(queue='task_creation_queue', on_message_callback=process_task)

            self.stdout.write('Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error connecting to RabbitMQ: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
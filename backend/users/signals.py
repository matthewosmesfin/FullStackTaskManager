from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .tasks import send_task_creation_message

User = get_user_model()  # Dynamically get the custom user model

@receiver(post_save, sender=User)
def create_task_for_new_user(sender, instance, created, **kwargs):
    if created:
        try:
            task_data = {
                'title': 'Welcome Task user',
                'description': 'Send a welcome email to the new user',
                'completed': False,
                'user': f'http://localhost:8000/users/{instance.id}/'
            }
            send_task_creation_message(task_data)
            print("Task creation message sent for new user")
        except Exception as e:
            print(f"Failed to create task: {e}")

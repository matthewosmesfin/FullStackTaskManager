#from django.contrib.auth.models import Group, User
# from django.contrib.auth.models import Group

from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from .serializers import UserSerializer
from .tasks import send_task_creation_message  # Import your RabbitMQ sending function
from rest_framework.permissions import IsAuthenticated  # Updated

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Changed to IsAuthenticated

    def perform_create(self, serializer):
        try:
            user = serializer.save()
            print(f"User created: {user.email}")

            # Prepare task data for the RabbitMQ message
            task_data = {
                'title': 'Welcome Task',
                'description': 'Send a welcome email to the new user',
                'completed': False,
                'user': f'http://localhost:8000/users/{user.id}/'
            }
            # Send task creation message
            send_task_creation_message(task_data)
        except Exception as e:
            print(f"Error in perform_create: {e}")


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
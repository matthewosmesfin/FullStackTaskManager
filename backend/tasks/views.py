from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Task.objects.all()  # Or use any filtering you want


    def get_queryset(self):
        """
        This view returns a list of all the tasks for the currently authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(user=user).order_by('-created_at')  # Filter tasks by user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user as the currently authenticated user

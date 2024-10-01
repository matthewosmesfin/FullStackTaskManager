from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):

    def setUp(self):
        # Create a user with both email and username
        self.user = User.objects.create_user(
            username='testuser', 
            email='testuser@example.com', 
            password='testpassword'
        )

class UserTests(APITestCase):

    def setUp(self):
        # Create a user with both email and username
        self.user = User.objects.create_user(
            username='testuser', 
            email='testuser@example.com', 
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')  # Log in the user

    def test_user_creation(self):
        url = reverse('users-list')  # Adjust the URL name based on your routing
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
        }
        response = self.client.post(url, data, format='json')
        
        # Print response data if the status code is not 201
        if response.status_code != status.HTTP_201_CREATED:
            print(f"Failed to create user: {response.status_code}, Response: {response.data}")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')  
        self.assertEqual(response.data['email'], 'newuser@example.com')  


class TaskTests(APITestCase):

    def setUp(self):
        # Create a user with both email and username
        self.user = User.objects.create_user(
            username='testuser', 
            email='testuser@example.com', 
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')  # Log in using username

    def test_create_task(self):
        url = reverse('task-list')  # Ensure this matches your router registration
        
        data = {
            'title': 'New Task',
            'description': 'Description for the new task',
            'completed': False,
            'user': f'http://localhost:8000/users/{self.user.id}/'
        }
        response = self.client.post(url, data, format='json')
        
        # Print response data if the status code is not 201
        if response.status_code != status.HTTP_201_CREATED:
            print(f"Failed to create task: {response.status_code}, Response: {response.data}")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user_tasks(self):
        url = reverse('task-list')  # Ensure this matches your router registration
        response = self.client.get(url, format='json')
        
        # Print response data if the status code is not 200
        if response.status_code != status.HTTP_200_OK:
            print(f"Failed to get user tasks: {response.status_code}, Response: {response.data}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

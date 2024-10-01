from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission
from django.db import models
from .managers import CustomUserManager  # Make sure you import the custom user manager

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Remove the groups field
    # groups = models.ManyToManyField(Group, related_name='custom_user_groups')  # Avoid clash
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')  # Avoid clash

    objects = CustomUserManager()  # Use the custom user manager

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

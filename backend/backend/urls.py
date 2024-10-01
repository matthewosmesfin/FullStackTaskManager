from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users import views as user_views  # Import the views from the users app
from tasks import views as task_views  # Import the views from the tasks app

from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
# router.register(r'groups', user_views.GroupViewSet)
router.register(r'tasks', task_views.TaskViewSet)  # Register the tasks viewset

urlpatterns = [
    # REST API
    path('', include(router.urls)),
    
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # REST API authentication
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

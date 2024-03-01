from django.urls import path
from .views import users_set

urlpatterns = [
        
    path('employee/',users_set,name='list_users'),
]
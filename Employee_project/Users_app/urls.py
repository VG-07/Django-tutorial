from django.urls import path
from . import views
urlpatterns = [
    path('',views.users_set,name='list_users'),
]
from django.urls import path
from vaibhavapp import views

urlpatterns = [
    path('pro/', views.display_profiles),
]
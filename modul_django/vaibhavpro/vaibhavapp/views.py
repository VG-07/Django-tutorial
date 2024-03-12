from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import UserProfile

def display_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'vaibhavapp/index.html', {'profiles': profiles})
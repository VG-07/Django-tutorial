from django.shortcuts import render
from .models import users

# Create your views here.

def users_set(request):
    employee=users.objects.all()
    return render(request,'index.html',{'employee': employee})
    

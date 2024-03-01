from django.shortcuts import render
from .models import users_form

# Create your views here.

def users_set(request):
    employee=users_form.objects.all()
    return render(request,'index.html',{'employee': employee})
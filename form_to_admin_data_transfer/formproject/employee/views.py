from django.shortcuts import render,redirect
from .forms import Employeeform
from .models import employee

def employee_form(request):
    if request.method=='POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employee_list')
    else:
        form = Employeeform()
    return render(request,'employee_form.html',{'form':form})
    
def employee_list(request):
    employees=employee.objects.all()
    return render(request,'employee_list.html',{'employees':employees})

# Create your views here.

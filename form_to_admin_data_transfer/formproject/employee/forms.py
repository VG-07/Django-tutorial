from django import forms
from .models import employee

class Employeeform(forms.ModelForm):
    class Meta:
        model = employee
        fields=['first_name','last_name','email','phone_number']
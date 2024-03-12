from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_form,name='form'),
    path('list/', views.employee_list,name='list'),
]
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from django.views.generic import ListView , DetailView
# Create your views here.
class PostView(ListView):
    model=Blog
    template_name='blog.html'
    queryset=Blog.objects.all()
    context_object_name='posts'

class DetailsView(DetailView):
    model=Blog
    context_object_name='post'
    template_name='blog_details.html'
    
class SearchView(ListView):
    model=Blog
    template_name='blog.html'
    context_object_name='posts'

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Blog.objects.filter(title_icontains=query).order_by('-created_at')


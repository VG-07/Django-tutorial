from django.urls import path
from . import views

urlpatterns= [
    path('',views.PostView.as_view(),name='post-list'),
    path('details/<int:pk>',views.DetailsView.as_view(),name='post_details'),
    path('search-blog',views.SearchView.as_view(),name='search_blog')
]
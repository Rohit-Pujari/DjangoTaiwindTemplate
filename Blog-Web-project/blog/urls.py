from django.urls import path, include
from . import views
from home.views import search
urlpatterns = [
    #API for handling comments
    path("postComment", views.postComment, name="postComment"),
    path('search',search, name="search"),
    path("", views.blogHome, name="blogHome"),
    path("<str:slug>", views.blogPost, name="blogPost"),
]

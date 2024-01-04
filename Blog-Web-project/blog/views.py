from django.shortcuts import render, HttpResponse
from .models import Post


# Create your views here.
def blogHome(request):
    allpost = Post.objects.all()
    context = {"allposts": allpost}
    return render(request, "blog/home.html",context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {"post": post}
    return render(request, "blog/post.html",context)
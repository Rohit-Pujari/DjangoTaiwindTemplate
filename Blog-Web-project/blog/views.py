from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
    return render(request, 'blog/home.html')

def blogPost(request,slug):
    slug = {'slug':slug}
    return render(request, 'blog/post.html', {'slug':slug})
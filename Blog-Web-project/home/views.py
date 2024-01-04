from django.shortcuts import render,redirect,HttpResponse
from . models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.
def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phonenumber"]
        content = request.POST["content"]
        if len(name)<2 or len(email)<2 or len(phone)<10 or len(content)<4:
            messages.error(request,"Fill the form correctly.")
            return redirect("contact")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"successfully sent your issue to the maintainer.")
            return redirect("contact")
    else:
        return render(request, "home/contact.html")

def search(request):
    query = request.GET['search']
    if len(query) == 0:
        messages.error(request,"cannot do empty search ")
        return redirect("/")
    if len(query) > 50:
        allposts = Post.objects.none()
    else:   
        allposts_title = Post.objects.filter(title__icontains=query)
        allposts_author = Post.objects.filter(author__icontains=query)
        allpost_content = Post.objects.filter(content__icontains=query)
        allposts = allposts_title.union(allposts_author,allpost_content)

    if allposts.count() == 0:
        messages.warning(request,"Invalid Search")
    context = {"allposts":allposts,
               "query":query}
    return render(request, "home/search.html",context)
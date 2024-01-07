from django.shortcuts import render,redirect,HttpResponse
from . models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    allblogs = Post.objects.all()
    blogs = {"allblogs": allblogs}
    return render(request, "home/home.html",blogs)


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

def signup(request):
    if request.method == "POST":
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if len(password1) < 5:
            messages.warning(request,"password must be at least 5 characters long")
            return redirect("/")
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken")
            return redirect("/")
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect("/")        
        if password1 != password2:
            messages.error(request,"Password must match")
            return redirect("/")
        print(username,password1,password2)
        user = User.objects.create_user(username=username, email=email, password=password2,first_name=firstname,last_name=lastname)
        user.save();
        messages.success(request,"Your account has been created successfully, please login")
        return redirect("/")
    else:
        messages.error(request," can not do empty SignUp submission")
        return redirect("/")


def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        user = authenticate(username=loginusername, password=loginpassword)
        print(user,loginpassword,loginusername)
        if user is not None:
            login(request, user);
            messages.success(request,"You have successfully logged in")
            return redirect("/")
        else:
            messages.error(request,"Username or password is incorrect")
            return redirect("/")
    return redirect("/")


def handlelogout(request):
    logout(request);
    messages.success(request,"Successfully logged out")
    return redirect("/")
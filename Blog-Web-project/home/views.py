from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "home/contact.html")

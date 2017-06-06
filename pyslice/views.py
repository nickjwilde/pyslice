from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pyslice/home.html", None)

def about(request):
    return render(request, "pyslice/about.html", None)

def contact(request):
    return render(request, "pyslice/contact.html", None)

def learn(request):
    return render(request, "pyslice/learn.html", None)

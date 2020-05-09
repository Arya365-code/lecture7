from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HTTPResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render)request, "users/login.html", {"message": None})
    context = {
        "use": request.user
    }
    return render(request, "users/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HTTPResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})
        
def logout_view(request):
    logout(request)
    return render(request, "users/logout.html", {"message": "Logged out."})
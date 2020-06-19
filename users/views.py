from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserForm
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
    user_form = UserForm()
    return render(request, "signup.html", {"user_form": user_form})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pwd"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            return render(
                request, "login.html", {"error": "username or password is incorrect."}
            )
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("index")


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from .models import *

User = get_user_model()


def AuthLogin(request):
    if request.method == "GET":
        return render(request, "./home/auth_login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            with transaction.atomic():
                user = User.objects.get(username = username)
        except User.DoesNotExist:
            messages.error(request, "Usuario ou senha incorretos.")
            return render(request, './home/auth_login.html')
        
        if check_password(password, user.password):
            login(request, user)
            return redirect(Index) 
        else:
            messages.error(request, "Usuario ou senha incorretos.")
            return render(request, './home/auth_login.html')
    

@login_required(login_url=AuthLogin)
def Base(request):
    return render(request, "./home/base.html")

@login_required(login_url=AuthLogin)
def Index(request):
    return render(request, "./home/index.html")

# Create your views here.

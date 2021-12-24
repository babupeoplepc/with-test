from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User


def test_page(request):
    return render(request, "users/testpage.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증 성공")
            login(request, user)
        else:
            print("인증 실패")
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("user:login")


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]

        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.firstname = firstname
        user.student_id = student_id
        user.save()
        print(request.POST)
        return redirect("user:login")
    return render(request, "users/signup.html")
    

# Create your views here.

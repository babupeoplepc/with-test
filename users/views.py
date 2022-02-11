from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User





def goto_javascript_study(request):
    return render(request, "users/javascript_study.html")


def goto_lesson_reservation(request):
    return render(request, "users/lesson_reservation.html")


def goto_block_test(request):
    return render(request, "users/block_test.html")


def goto_css_study(request):
    return render(request, "users/css_study.html")


def goto_dashboard(request):
    return render(request, "users/dashboard.html")


def test_page(request):
    return render(request, "users/testpage.html")


def login_view(request):
    if request.method == "POST":
        print(request.POST)
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
        
        print(request.POST)
        
        username = request.POST["student_email"]
        password = request.POST["student_password"]
        email = request.POST["student_email"]
        user = User.objects.create_user(username, email, password)

        user.student_name = request.POST["student_name"]
        user.student_gender = request.POST["student_gender"]
        user.student_email = request.POST["student_email"]
        user.student_phone_number = request.POST["student_phone_number"]
        user.student_birth_year = request.POST["student_birth_year"]
        user.student_birth_month = request.POST["student_birth_month"]
        user.student_birth_day = request.POST["student_birth_day"]
        user.student_home_address = request.POST["student_home_address"]
        user.student_job = request.POST["student_job"]
        user.student_visit = request.POST["student_visit"]
        user.student_visit_example = request.POST["student_visit_example"]
        user.student_comment = request.POST["student_comment"]
        user.student_lesson_comment = request.POST["student_lesson_comment"]
        
        if 'student_push_stop' in request.POST:
            print("on")
            if request.POST["student_push_stop"] == "on":
                user.student_push_stop = "on"

        
        user.save()
        
             
            
        

        

        
        return redirect("user:login")
    return render(request, "users/signup.html")
    

# Create your views here.

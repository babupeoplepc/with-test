from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("test/", views.test_page, name="test_page"),
    path("dashboard/", views.goto_dashboard, name="dashboard_page"),
    path("css_study/", views.goto_css_study, name="css_study_page"),
    path("block_test/", views.goto_block_test, name="block_test_page"),
    path("lesson_reservation/", views.goto_lesson_reservation, name="lesson_reservation_page"),
    path("javascript_study/", views.goto_javascript_study, name="javascript_study_page"),
]
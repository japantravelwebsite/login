from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path("login", views.login_view, name = 'login'), # login path 설정
    path("logout", views.logout_view, name = 'logout'), # logout path 설정
    path("signup", views.signup_view, name = 'signup') # signup path 설정
]
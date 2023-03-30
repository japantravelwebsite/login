from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings
app_name = 'user'

urlpatterns = [
    path("login", views.login_view, name = 'login'), # login path 설정
    path("logout", views.logout_view, name = 'logout'), # logout path 설정
    path("signup", views.signup_view, name = 'signup'), # signup path 설정
    path("Chubu/Nagoya", views.GetNagoya, name = 'Nagoya'), # l
    path("Chubu/Takayama", views.GetTakayama, name = 'Takayama'), # l
    path("Chubu/Toyama", views.GetToyama, name = 'Toyama'), # 
    path("Chubu/Gero", views.GetGero, name = 'Gero'), # 
    path("login", views.GetBacktoLogin, name = 'GetBacktoLogin'), # 
    path("Chubu", views.Chubu_view, name = 'Chubu'), # jubu path 설정
    path("Wrong", views.Wrong_view, name="Wrong"),# 주부말고 다른거누를때
    path("Chubu/choice", views.choice_view, name="choice"),
    path("Chubu/choice_gero", views.choice_gero_view, name="choice_gero"),
    path("Chubu/choice_toyama", views.choice_toyama_view, name="choice_toyama"),
    path("Chubu/choice_nagoya", views.choice_nagoya_view, name="choice_nagoya"),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
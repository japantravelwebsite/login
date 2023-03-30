from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from .models import picture_db
import time
from django.db import connection
from django.shortcuts import render

import logging
logger = logging.getLogger('my')
# Create your views here.
login_user_name = 'None'

def login_view(request):
    logger.info("LOGIN INFO")
    msg = "_"
    if request.method == "POST":
#        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        global login_user_name
        login_user_name = username
        print(login_user_name)
        user = authenticate(username = username, password = password)
        if user is not None:
            print("인증성공")
            msg = "로그인성공"
            login(request, user)
        else:
            print("인증실패")
            messages.info(request, "입력이 잘못되었습니다.")
            msg = "입력실패"
            
    return render(request, "users/login2.html",{'msg':msg})#20230312김정현

def logout_view(request):
    logger.info("%s LOGOUT INFO", login_user_name)
    logout(request)
    return redirect("user:login")

def signup_view(request):
    logger.info("SIGNUP INFO")
    msg = "_"
    if request.method == "POST":
        username =request.POST["username"]
        password =request.POST["password"]
        firstname =request.POST["firstname"]
        lastname =request.POST["lastname"]
        email =request.POST["email"]
        student_id =request.POST["student_id"]

        if len(username)*len(password)*len(firstname)*len(lastname)*len(email)*len(student_id) != 0: 
            print(request.POST)
            user = User.objects.create_user(username, email, password)
            user.last_name = lastname
            user.first_name = firstname
            user.student_id = student_id
            user.save()
            return redirect("user:login")
        else:
            print("빈칸오류")
            msg = "빈칸을 모두 채워주세요"
            # messages.info(request, "빈칸을 모두 채워주세요")
    return render(request, "users/signup.html",{'msg':msg})

def GetNagoya(request):
    print(login_user_name)
    logger.info("%s NAGOYA INFO", login_user_name)
    #imgs = picture_db.objects.get(location = "Nagoya")
    return render(request, "users/Nagoya.html")
def GetTakayama(request):
    logger.info("%s TAKAYAMA INFO", login_user_name)
    imgs = picture_db.objects.filter(location = "Takayama")
    return render(request, "users/Takayama.html", {"imgs" : imgs})
def GetToyama(request):
    logger.info("%s TOYAMA INFO", login_user_name)
    #imgs = picture_db.objects.get(location = "Toyama")
    return render(request, "users/Toyama.html", login_user_name)
def GetGero(request):
    logger.info("%s GERO INFO", login_user_name)
    #imgs = picture_db.objects.get(location = "Gero")
    return render(request, "users/Gero.html")
def GetBacktoLogin():
    logger.info("%s GETBACKTO INFO", login_user_name)
    return redirect("user:login")
def Chubu_view(request):
    logger.info("%s CHUBU INFO", login_user_name)
    return render(request, "users/Chubu.html")
def Wrong_view(request):  
    logger.info("%s WRONGINFO", login_user_name)
    msg = 0
    if msg ==0:
        msg +=1
        return render(request,"users/Wrong.html")
        time.sleep(3)
        
    return redirect("user:login")

def choice_view(request):
    logger.info("%s CHOICE TAKAYAMA INFO", login_user_name)
    return render(request, "users/choice.html")

def choice_gero_view(request):
    logger.info("%s CHOICE GERO INFO", login_user_name)
    return render(request, "users/choice_gero.html")

def choice_nagoya_view(request):
    logger.info("%s CHOICE NAGOYA INFO", login_user_name)
    return render(request, "users/choice_nagoya.html")

def choice_toyama_view(request):
    logger.info("%s CHOICE TOYAMA INFO", login_user_name)
    return render(request, "users/choice_toyama.html")


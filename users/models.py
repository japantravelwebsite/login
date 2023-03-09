from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser): #상속 받아 사용
    student_id = models.CharField(max_length=10) # student_id만 따로 추가 정의 


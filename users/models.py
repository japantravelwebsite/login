from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser): #상속 받아 사용
    student_id = models.CharField(max_length=10) # student_id만 따로 추가 정의 

class blogdb(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)

class picture_db(models.Model):
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    etc1 = models.CharField(max_length=100)
    etc2 = models.CharField(max_length=100)
    etc3 = models.CharField(max_length=100)






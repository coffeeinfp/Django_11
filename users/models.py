from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20) #이름
    description = models.TextField() #긴문자열
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=5)# 성별

    
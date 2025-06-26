from django.db import models
from common.models import CommonModel


class Board(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)



    def __str__(self): 
        return self.title
#__str__ 객체를 사람이 읽기 좋은 문자열로 표현해줘 

# 모델변경사항감지마이그래이션파일생성: python manage.py makemigrations
# python manage.py migrate : 생선된 migrations파일 db 적용
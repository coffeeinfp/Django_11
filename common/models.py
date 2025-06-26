from django.db import models

class CommonModel(models.Model):
    #auto_now_add :현재 데이터 생성 시간 기준으로 생성->이후데이터 업데이트 되도 수정 안됨
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now : 생성 시간 기준 으로 일단생성됨->이후데이터 업데이트 되면 현재시간도 수정됨
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #db 테이블에 위와 같은 컬럼이 추가되지 않음
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
     list_display = ("username", "email", "is_business","grade")
     fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


# @-데코레이터 클래스에 특별한 기능 추가
# @admin.register(User) - User모델을 관리자페이지(admin)에 등록
#(admin.ModelAdmin)- 장고 제공 기본 관리자 전용 기능 상속= 넘겨줌


#python manage.py makemigrations
# -modely.py을 기반으로 db에 적용할 준비파일을 만드는 명령어
# db 적용 준비파일 -> 0001_initial.py


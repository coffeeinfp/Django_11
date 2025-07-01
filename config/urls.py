from django.contrib import admin  #Django 기본 제공 관리자admin기능
from django.urls import path,include  #path()함수-url과view 매핑
from feeds import views  #feeds 앱의 views.py 안에 있는 함수 가져옴

urlpatterns = [
    path('admin/', admin.site.urls),  
    path("api/v1/feeds/",include("feeds.urls")),
   
]


#언제쓰는 코드인가? url을 통해 변수도 넘기고, 주소에 따라 다른 뷰를 보여주고싶을 때
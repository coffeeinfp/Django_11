"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  #Django 기본 제공 관리자admin기능
from django.urls import path   #path()함수-url과view 매핑
from feeds import views  #feeds 앱의 views.py 안에 있는 함수 가져옴

urlpatterns = [
    path('admin/', admin.site.urls),  
    path("feeds/", views.show_feed),
    path("feeds/all",views.all_feed),
    path("feeds/<int:feed_id>/<str:feed_content",views.one_feed)
]


#언제쓰는 코드인가? url을 통해 변수도 넘기고, 주소에 따라 다른 뷰를 보여주고싶을 때
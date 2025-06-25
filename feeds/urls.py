from django.urls import path
# djago.url-장고안의urls라는모듈에서 path가져와
# path-url경로정의함수
from . import views # 현재 디렉토리의 views.py 불러오기

urlpatterns = [ 
    path("", views.show_feed),
    path("<int:feed_id>/<str:feed_content>/",views.all_feed),
]

#urlpatterns -url목록/리스트
from django.shortcuts import render
#render는 지금은 안쓰지만 미리 가져다 놓음
from django.http import HttpResponse
#HttpResonsesms 텍스트나 간단한 메시지를 웹 브라우저에 그대로 응답



def show_feed(request):
    return HttpResponse("show feed")

def one_feed(request, feed_id, feed_content):
    return HttpResponse(f"feed_id: {feed_id},{feed_content}")

def all_feed(request):
    return HttpResponse("all feed")

 

#request란?-사용자의요청정보가 들어간 변수
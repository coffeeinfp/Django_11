from django.test import TestCase
from django.http import HttpResponse
# Create your tests here.

def show_feed(request):
    return HttpResponse("show feeed")


from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request): # @app.route('') 아래 def index의 기능을 views.py가 한다.
    print(request)
    print(type(request))
    print(request.META)
    return HttpResponse('hello, django!')
import random
import datetime
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request): # @app.route('') 아래 def index의 기능을 views.py가 한다.
    print(request)
    print(type(request))
    print(request.META)
    return render(request, 'index.html')
    
def dinner(request):
    box = ['처갓집치킨', 'BHC치킨', '햄버거', '식빵', '토스트', '고구마맛탕', '피자', '핫도그', '충만치킨',' 삼합', 'emoi', '푸라닭치킨']
    pick = random.choice(box)
    # return HttpResponse(dinner)
    # render 필수인자
    # 1) request, 2) template 파일(html)
    # render 선택인자
    # 3) dictionary : 템플릿에서 쓸 변수 값을 정의
    return render(request, 'dinner.html', {'dinner': pick, 'box': box})
    # return ('dinner.html', dinner=dinner, box=box)
    # template은 기본적으로 문법이 jinja2랑 비슷한데, 장고에서는 DTL을 쓴다.
    # Django Template Language
    
def you(request, name):
    return render(request, 'you.html', {'name': name})
    
def cube(request, num):
    return render(request, 'cube.html', {'num': num, 'result': num**3})
    
def ping(request):
    return render(request, 'ping.html')

def pong(request):
    print(request.GET)
    msg = request.GET.get('message')
    return render(request, 'pong.html', {'msg': msg})
    
def user_new(request):
    return render(request, 'user_new.html')
    
def user_read(request):
    user_id = request.POST.get('user_id')
    user_password = request.POST.get('user_password')
    return render(request, 'user_read.html', {'user_id': user_id, 
    'user_password': user_password}) 
    
def template_example(request):
    my_dict = {'name': 'kim', 'nickname': 'sh', 'age': 20}
    my_list = ['폭찹', '김치볶음밥', '짬뽕']
    my_sentence = 'Life is short, you need python!'
    messages = ['applge', 'banana', 'cucumber', 'mango']
    now = datetime.datetime.now()
    empty_list = []
    return render(request, 'template_example.html', {'my_dict': my_dict, 'my_list': my_list, 
    'my_sentence': my_sentence, 'messages': messages, 'now': now, 'empty_list': empty_list})
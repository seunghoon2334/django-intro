import random
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
    
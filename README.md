# Django

## 1. 시작하기

1. 프로젝트 시작하기

   ```bash
   $ django-admin startproject 프로젝트이름
   ```

   아래와 같이 프로젝트 구조가 만들어진다.

   ```text
   ├── db.sqlite3
   ├── django_intro
   │   ├── __init__.py
   │   ├── __pycache__
   │   │   ├── __init__.cpython-36.pyc
   │   │   ├── settings.cpython-36.pyc
   │   │   ├── urls.cpython-36.pyc
   │   │   └── wsgi.cpython-36.pyc
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   └── manage.py
   ```

   지금부터 pwd는 `~/workspace/django_intro`이다.

2. 서버 실행하기

- `settings.py` 설정

```python
     AllWED_HOST = ['*']
    # c9에서는 host - 0.0.0.0, port - 8080 만 활용할 수 있기 때문에 위와 같이 설정한다.
```

```bash
   ~/workspace/django_intro $python manage.py runserver 0.0.0.0:8080
```

앞으로 모든 장고 명령어는 프로젝트를 만들 때를 제외하고 `python manage.py`를 활용한다. 따라서, 명령어가 안될 때에는 반드시 `pwd`와 `ls`를 통해 현재 bash(터미널) 위치를 확인하자!!

# Hello, Django

> Django 프로젝트는 여러가지 app의 집합이다.
>
> 각각의 app은  MTV 패턴으로 구성되어 있다.
>
> M (Model) : 어플리케이션의  핵심 로직의 동작을 수행한다.
>
> T (Template) : 사용자에게 결과물을 보여준다.
>
> V (View) : 모델과 템플릿의 동작을 제어한다. (모델의 상태를 변경하거나 값을 가져오고, 템플릿에 값을 전달하기 등)
>
> **일반적으로 MVC패턴으로  더 많이 사용된다.**

### 기본 로직

앞으로 우리는 1. 요청 url 설정(`urls.py`) 2. 처리 할 view 설정(`views.py`) 3. 결과 보여줄 template 설정(`templates/`)으로 작성할 것이다. 

1. url 설정

   ```python
   # django_intro/urls.py
   from django.contrib import admin # @app.route('')의 기능을 urls.py가 한다.
   from django.urls import path
   # home 폴더 내에 있는 views.py를 불러온다.
   from home import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       # 요청이 home/으로 오면, views의 index 함수를 실행시킨다.
       path('home/', views.index)
   ]
   ```

2. view 설정

```python
   # home/views.py
   from django.shortcuts import render, HttpResponse
   
   # Create your views here.
   def index(request): # @app.route('') 아래 def index의 기능을 views.py가 한다.
       return HttpResponse('hello, django!')
```

- 주의할 점은 선언된 함수에서 `request`를 인자로 받아야 한다.
  - request는 사용자(클라이언트)의 요청 정보와 서버에 대한 정보가 담겨 있다.
  - Django 내부에서 해당 함수를 호출하면서 정보를 넘겨주기 때문에 반드시 명시해줘야한다.

# Template (MTV - T)

> Django에서 활용되는 Template은 DTL(Django Template Language)이다.
>
> jinja2와 문법이 유사하다.

1. 요청 url 설정

   ```python
   path('home/dinner/', views.dinner)
   ```

2. view 설정

```python
   def dinner(request):
       box = ['치킨', '밥', '피자']
       pick = random.choice(box)
       return render(request, 'dinner.html', {'dinner': pick})
```

- Template을 리턴하려면, `render`를 사용하여야 한다.
  - request (필수)
  - `template 파일 이름` (필수)
  - `template 변수` (선택) : `dictionary` 타입으로 구성해야 한다.

1. Template 설정

   ```bash
   $ mkdir home/templates
   $ touch home/templates/dinner.html
   ```

   ```html
   <!-- home/templates/dinner.html -->
   <h1> {{pick}} </h1>Variable Routing
   ```

![1234](image/1234.jpg)

# Variable Routing

1. url 설정

   ```python
   path('home/you/<name>', views.you),
   path('home/cube/<int:num>', views.cube)
   ```

2. view 파일 설정

   ```python
   def you(request, name):
       return render(request, 'you.html', {'name': name})
   ```

3. 템플릿 파일 설정

   ```django
   <h1> {{ name }}, 안녕!!! </h1>
   ```



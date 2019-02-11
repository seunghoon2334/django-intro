"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin # @app.route('')의 기능을 urls.py가 한다.
from django.urls import path
# home 폴더 내에 있는 views.py를 불러온다.
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 요청이 home/으로 오면, views의 index 함수를 실행시킨다.
    path('home/', views.index),
    path('home/dinner/', views.dinner),
    path('home/you/<name>/', views.you),
    path('home/cube/<int:num>/', views.cube),
]
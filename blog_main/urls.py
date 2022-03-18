"""blog_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

#1st router

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

# 이 urls.py가 1차 라우터
# include('blog.urls') 블로그 안에 있는 urls.py가 2차적 으로 라우팅
# blog.urls 안에 있는 view.py가 실제 function(정적 렌더링)
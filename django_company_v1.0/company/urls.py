"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from home import views as home_view
urlpatterns = [
    #path("index/", home_view.index),   #网址需输入http://127.0.0.1:8000/index
    path(r"", home_view.index),          #网址输入http://127.0.0.1:8000/即可
    re_path(r"^index/$", home_view.index, name="index"),
    re_path(r"^about/$", home_view.about, name="about"),
    re_path(r"^news/$", home_view.news, name="news"),
    re_path(r"^contact/$", home_view.contact, name="contact"),
    path('admin/', admin.site.urls),
]

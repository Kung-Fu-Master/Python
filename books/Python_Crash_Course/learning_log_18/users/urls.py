from django.contrib.auth.views import LoginView
from django.urls import path, re_path
from . import views

"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""

app_name = 'users'

urlpatterns = [
    #login page
    path('',LoginView.as_view(template_name='users/login.html'),name="login"),
    path(r"^logout/$", views.logout_view, name="logout"),

    #register page
    #path(r"^register/$", views.register, name="register"),
    re_path(r'^register/$', views.register, name='register'), # 与URL http://localhost:8000/users/register/匹配， 并将请求发送给我们即将编写的函数register()
]



from django.contrib.auth.views import LoginView
from django.urls import path
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
    path(r"", views.logout_view, name="logout"),
]



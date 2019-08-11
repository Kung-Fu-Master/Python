from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def logout_view(request):
    #logout user
    logout(request)
    return HttpResponseRedirect(reverse("learning_logs:index"))
"""
def register(request):
    #register new user
    if request.method != "POST":
        form = UserCreationForm()
    else:
        #process the complete form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #let users automatically log in and redirect to the home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST["password1"])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("learning_logs:index"))
    context = {"form":form}
    return render(request, "users/register.html", context)
"""

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单   
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录， 再重定向到主页
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form} 
    return render(request, 'users/register.html', context)
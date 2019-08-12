from django.shortcuts import render
from home.models import *
# Create your views here.

def index(request):
    title = Webname.objects.filter()[0]
    return render(request, 'home/index.html', {'title':title})

def about(request):
    title = Webname.objects.filter()[0]
    about_content = News.objects.filter(link='2')[0]
    return render(request, 'home/about.html',{'title':title, 'about_content':about_content})

def news(request):
    title = Webname.objects.filter()[0]
    return render(request, 'home/news.html',{'title':title})

def contact(request):
    contact_content = News.objects.filter(link='2')[0]
    title = Webname.objects.filter()[0]
    return render(request, 'home/contact.html',{'title':title, 'contact_content':contact_content})

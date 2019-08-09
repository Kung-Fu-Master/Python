from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    return render(request, "learning_logs/index.html")

def topics(request):
    #show all topics
    topics = Topic.objects.order_by("date_added")
    context = {"topics":topics}
    return render(request, "learning_logs/topics.html", context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {"topic":topic, "entries":entries}
    return render(request, "learning_logs/topic.html", context)

def new_topic(request):
    #add new topic
    if request.method != "POST":
        #unsubmitted data, create a new form
        form = TopicForm()
    else:
        #POST submitted data, processing data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:topics"))
    context = {"form":form}
    return render(request, "learning_logs/new_topic.html", context)

def new_entry(request, topic_id):
    #add a new entry to a specific topic
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic_id]))
    context = {"topic":topic, "form":form}
    return render(request, "learning_logs/new_entry.html", context)

def edit_entry(request, entry_id):
    #edit existing entries
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        #initial request, fill the form with the current entry
        form = EntryForm(instance=entry)
    else:
        #POST submitted data, processing data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs:topic", args=[topic.id]))
    context = {"entry":entry, "topic":topic, "form":form}
    return render(request, "learning_logs/edit_entry.html", context)
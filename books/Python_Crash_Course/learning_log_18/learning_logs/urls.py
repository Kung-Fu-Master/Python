from django.urls import path
from . import views

urlpatterns = [
    #main page
    path("", views.index, name="index"),

    #show all topics
    path(r"^topics/$", views.topics, name="topics"),

    #detailed page for a specific page
    path(r"^topics/(?P<topic_id>\d+)/$", views.topic, name="topic"),

    #web page to add a new topic
    path(r"^new_topic/$", views.new_topic, name="new_topic"),

    #page to add new entries
    path(r"^new_entry/(?P<topic_id>\d+)/$", views.new_entry, name="new_entry"),

    #page for editing entries
    path(r"^edit_entry/(?P<entry_id>d+)/$", views.edit_entry, name="edit_entry"),
]
app_name = 'learning_logs'
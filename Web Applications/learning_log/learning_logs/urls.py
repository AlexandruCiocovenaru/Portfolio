"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views # import view from the same directory as urls.py

# distinguish the app from other apps in the project
app_name = 'learning_logs'

# set up a list of individual pages that can be requested from the learning_logs app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry
    path ('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
] # use path function and enter three params:
# '' parameter is set to ignore the base URL, in order to help Django route the URL request to the proper view
# views parameter is set to call the function 'index' to match the URL request with the defined URL pattern
# name parameter defines the name 'index' for the requested URL pattern

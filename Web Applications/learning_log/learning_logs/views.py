from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry # import the data associated with the data we need
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html') # process the URL request and render a template


@login_required # apply decorator to run login_required function first, if the user isn't logged in return to login page
def topics(request): # the function needs the URL request parameter
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # retrieve from database the topic objects
    # with the same owner attribute, sort them by the attribute 'date_added' and store the queryset in 'topics'
    context = {'topics': topics} # define a context dict to be sent to the html template and access the data by key
    return render(request, 'learning_logs/topics.html', context) # add also the context to be rendered in the html page


@login_required
def topic(request, topic_id): # the function accepts also the value of topic_id param
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id) # use get function to query the database and retrieve the topic
    # Make sure the topic belongs to the current user
    if topic.owner != request.user: # if the user Topic doesn't match with the current logged user raise 404
        raise Http404

    entries = topic.entry_set.order_by('-date_added') # query the database for associated entries and sort them
    # "-" sign in front of date_added is to sort them in reverse (newest entries first)
    context = {'topic': topic, 'entries': entries} # store data in a dict context
    return render(request, 'learning_logs/topic.html', context) # send context dict to an html template


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST': # the user is submitting a GET request, we need to return a blank form
        # No data submitted; create a blank form.
        form = TopicForm() # create a empty form object and sent it to context dict
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST) # instantiate a TopicForm object and pass the data entered by the user
        if form.is_valid(): # before submitting to the database, check if the data matches the expected filed type
            new_topic = form.save(commit=False) # pass the commit=False argument to modify the new topic before
            # saving it to the database
            new_topic.owner = request.user # set the new topic’s owner attribute to the current user
            new_topic.save() # save the new topic instance
            return redirect('learning_logs:topics') # redirect the user to the topics page

    # Display a blank or valid form.
    context = {'form': form} # save the info in the context dict variable
    return render(request, 'learning_logs/new_topic.html', context) # render the info in an html page


@login_required
def new_entry(request, topic_id):
    """Add a new entry for every particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # Post data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # tell Django to create a new entry object and assign it to new_entry
            # without saving it to the database yet.
            new_entry.topic = topic # set the topic attribute of new_entry to the topic we pulled from the database at
            # the beginning of the function
            new_entry.save() # save the entry to the database with the correct associated topic.
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-filled form with the current entry.
        form = EntryForm(instance=entry, data=request.POST) # add an 'instance argument' to create a form prefilled with
        # the information from the existing entry object
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST) # create a form instance based on the information associated
        # with the existing entry object, updated with any relevant data from request.POST
        if form.is_valid():
            form.save()
            return redirect('learning_logs/topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

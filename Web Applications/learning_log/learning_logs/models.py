from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200) # CharField function to store small amount of text in a database
    # and add max_length as param to set up the storage space
    date_added = models.DateTimeField(auto_now_add=True) # DateTimeField function to store data about time and date
    # and add auto_now_add as param to automatically set the current date and time
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): # define a method to display a simple model string representation
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # ForeignKey function to link data to another record
    # in a database (our case Topic) and add one_delete param with CASCADE function to delete all entries when an
    # associated topic is deleted
    text = models.TextField() # TextField function to store any size limit of data in the database
    date_added = models.DateTimeField(auto_now_add=True)

    # next in Entry class another class called Meta, which stores extra info for managing the model
    class Meta:
        verbose_name_plural = 'entries' # use str 'entries' when referring to more than 1 entry

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..." # because an entry log can be long, we limit to show just the first 50 chars

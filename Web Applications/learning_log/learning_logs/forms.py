from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm): # define a class called TopicForm, which inherits from forms .ModelForm
    class Meta: # a nested Meta class telling Django which model to base the form on and which fields to include
        model = Topic # build a form from the Topic model
        fields = ['text'] # include a text filed
        labels = {'text': ''} # do not generate a label for the text field above


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # set up a widget HTML form element (drop down list,
        # multi-line text are etc.) and override Django's default settings using .forms.Textarea and expand the 'text'
        # area from 40 columns to 80 columns

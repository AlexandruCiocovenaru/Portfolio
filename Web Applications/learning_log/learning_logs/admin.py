from django.contrib import admin

# Register your models here.
from.models import Topic, Entry
admin.site.register(Topic) # use the function to manage our models through the admin page
admin.site.register(Entry)
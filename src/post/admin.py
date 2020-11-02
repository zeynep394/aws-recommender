#from django.contrib import admin

#from .models import  Post

#admin.site.register(Post)

from django.contrib import admin
from django.db.models import Model
import inspect
from . import models 

for name, Post in inspect.getmembers(models):
    if inspect.isclass(Post) and issubclass(Post, Model):
        admin.site.register(Post)
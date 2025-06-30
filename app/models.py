
from django.db import models
from django.db.models import Model, CharField, EmailField, SmallIntegerField, TextField, DateTimeField, ForeignKey, \
    CASCADE,URLField


# Create your models here.

class Category(Model):
    name = CharField(max_length=77)
    icon = URLField()

class Author(Model):
    fullname = CharField(max_length=50)
    email = EmailField(max_length=60,unique = True)
    password =CharField(max_length=50)
    age = SmallIntegerField()
    bio = TextField()
    registered_date  = DateTimeField(auto_now_add=True)

class Post(Model):
    title = CharField(max_length=200)
    description = TextField()
    author = ForeignKey('app.Author',on_delete=CASCADE,related_name='posts')
    category = ForeignKey('app.Category',on_delete=CASCADE,related_name='posts')
    created_at  = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

from django.db.models import EmailField,SmallIntegerField,TextField
from django.forms import ModelForm, Form, CharField

from app.models import Author,Post


class AuthorFormModel(ModelForm):
    class Meta:
        model = Author
        fields = 'fullname' , 'email' , 'password', 'age' , 'bio'

class PostFormModel(ModelForm):
    class Meta:
        model = Post
        fields = 'title' , 'description' , 'author' , 'category'

class PostFilterForm(Form):
    title = CharField(max_length=50 , required = False)
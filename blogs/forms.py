from django import forms
from django.forms.models import ModelForm
from django.core.validators import RegexValidator

from .models import Blog, Post


class BlogForm(ModelForm):
    url = forms.CharField(required=True, max_length=32,
                            validators=[
                                RegexValidator(
                                regex = r'^[a-zA-Z0-9-_.]+$',
                                message='Invalid URL name!',
                                code='invalid_url')])


    class Meta:
        model = Blog
        fields = ['title', 'description', 'url']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

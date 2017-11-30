from django.forms.models import ModelForm

from .models import Blog, Post

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

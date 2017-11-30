from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('auth.User',
                            on_delete=models.CASCADE,
                            related_name='blogs')

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    blog = models.ForeignKey('blogs.Blog',
                            on_delete=models.CASCADE,
                            related_name='posts')

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    body = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey('blogs.Post',
                            on_delete=models.CASCADE,
                            related_name='comments')
    user = models.ForeignKey('auth.User', related_name='comments')

    class Meta:
        ordering = ['-created_at']

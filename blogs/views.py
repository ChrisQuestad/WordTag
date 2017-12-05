from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse


from .models import Blog, Post, Comment
from .forms import BlogForm, PostForm


@method_decorator(login_required, name='dispatch')
class HomePageView(View):
    template_name = 'blogs/home.html'

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(user=request.user)

        return render(request, self.template_name, {'blogs':blogs})

@method_decorator(login_required, name='dispatch')
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/detail.html'

    def delete(self, request, *args, **kwargs):
        model = Blog.objects.get(pk=self.kwargs['pk'])
        if model.user == request.user and request.is_ajax():
            model.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=402)


@method_decorator(login_required, name='dispatch')
class BlogCreateView(View):
    form_class = BlogForm
    template_name = 'blogs/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.save()
            return redirect('blogs:detail', pk=model.pk)

        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post/detail.html'

    def get_queryset(self):
        return Post.objects.filter(blog__pk=self.kwargs['blog_pk'])

    def delete(self, request, *args, **kwargs):
        model = Post.objects.get(pk=self.kwargs['pk'])
        if model.blog.user == request.user and request.is_ajax():
            model.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=402)



@method_decorator(login_required, name='dispatch')
class PostCreateView(View):
    form_class = PostForm
    template_name = 'blogs/post/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        blog = Blog.objects.get(pk=self.kwargs['blog_pk'])

        if not blog.user == request.user:
            return HttpResponse(status=402)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        blog = Blog.objects.get(pk=self.kwargs['blog_pk'])
        if form.is_valid() and blog.user == request.user:
            model = form.save(commit=False)
            model.blog = blog
            model.user = request.user
            model.save()
            return redirect('blogs:post-detail', blog_pk=blog.pk, pk=model.pk)

        return render(request, self.template_name, {'form': form})

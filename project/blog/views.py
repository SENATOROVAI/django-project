from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

class PostView(View):
    '''records output'''
    def get(self, request):
        post = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': post})



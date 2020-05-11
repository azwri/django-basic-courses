from django.shortcuts import render
from .models import Post


def post_list(request):
  all_posts = Post.objects.all()
  return render(request, 'blog/all_posts.html', {'posts':all_posts})

def post_detail(request, id):
  post_detail = Post.objects.get(id=id)
  return render(request, 'blog/post_detail.html', {'post':post_detail})

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Comment, Post
from .forms import PostForm

# TODO: check if the user is authenticated on each endpoint

def posts(request):
  posts = Post.objects.all().order_by('-timestamp')
  form = PostForm()
  return render(request, 'posts/index.html', {
    'form': form,
    'posts': posts
  })

def post(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  return render(request, 'posts/detail.html', {
    'post': post
  })

def get_posts(request):
  posts = Post.objects.all().values()
  return HttpResponse(str({
    'posts': [post for post in posts]
  }))

def get_post_by_id(request, post_id):
  post = get_object_or_404(Post, pk=post_id).__dict__
  return HttpResponse(str(post))

def write_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      new_post = Post(title=data.get("title"), text=data.get("text"))
      new_post.save()
      return HttpResponseRedirect(reverse("posts:posts"))
    else:
      return HttpResponseBadRequest("Invalid data for the post.")
  else:
    return HttpResponseBadRequest("Method not allowed!")

def write_comment(request, post_id):
  if request.method == 'POST':
    comment_text = request.POST.get('comment')
    new_comment = Comment(text=comment_text, post_id=post_id)
    new_comment.save()
    return HttpResponseRedirect(reverse("posts:post", args=(str(post_id))))
  else:
    return HttpResponseBadRequest("Method not allowed!")
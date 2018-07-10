from __future__ import unicode_literals

from .models import Post, Comment
from datetime import datetime
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-total_upvotes')
    context = {'posts': posts,}
    return render(request, 'bugs/post_list.html', context)
    
def post_detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    comments = Comment.objects.filter(post=post).order_by('-id')
    post.views += 1
    post.save()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=post, user=request.user, content=content)
            comment.save()
    
    else:
        comment_form = CommentForm()
            
    context = {'post': post, 'comments': comments, 'comment_form': comment_form,}
    return render(request, 'bugs/post_detail.html', context)


@login_required
def upvote_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_upvoted = False
    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
        is_upvoted = False
    else:
        post.upvotes.add(request.user)
        is_upvoted = True
    return HttpResponseRedirect(post.get_absolute_url())


@login_required    
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostCreateForm()
    context = {'form': form,}
    return render(request, 'bugs/post_create.html', context)
    

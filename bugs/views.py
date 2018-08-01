from __future__ import unicode_literals
from .models import Post, Comment
from datetime import datetime
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count

# Create your views here.
def post_list(request):
    posts = Post.objects.annotate(comments=Count('comment'))
    for post in posts:
        post.total_upvotes = post.upvotes.count()
    context = {'posts': posts,}
    return render(request, 'bugs/post_list.html', context)
    
def post_detail(request, id, slug):
    post = get_object_or_404(Post, pk=id, slug=slug)
    is_upvoted = False
    if post.upvotes.filter(id=request.user.id).exists():
        is_upvoted = True
    comments = Comment.objects.filter(post=post, reply=None).order_by('id')
    post.views += 1
    post.save()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    
    else:
        comment_form = CommentForm()
            
    context = {'post': post, 'comments': comments, 
                'comment_form': comment_form, 'total_upvotes': post.total_upvotes(), 'is_upvoted' : is_upvoted}
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
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostCreateForm()
    context = {'form': form,}
    return render(request, 'bugs/post_create.html', context)
    
@login_required 
def post_update(request, id, slug):
    instance = get_object_or_404(Post, id=id)
    form = PostCreateForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "bugs/post_create.html", context)
        
    

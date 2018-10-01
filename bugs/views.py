from __future__ import unicode_literals
from .models import Post, Comment
from datetime import datetime
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count


# Retrieves list of open and working bug posts, excluding closed bugs.
# Annotates related comments count
def post_list(request):
    posts = Post.objects.exclude(status=3).annotate(comments=Count('comment'))
    context = {'posts': posts}
    return render(request, 'bugs/post_list.html', context)


# Retrieves post details
def post_detail(request, id, slug):
    # Retrieves post details base on primary key, is_upvoted variable
    # is automatically set to False
    post = get_object_or_404(Post, pk=id, slug=slug)
    is_upvoted = False
    # Checks if current user has previously upvoted the post and adjusts
    # up_voted variable to give user the option to downvote instead.
    if post.upvotes.filter(id=request.user.id).exists():
        is_upvoted = True
        # Finds comments that are related to particular post,
        # excluding comments which are replies to comments. Adjust like option
        #  for each comment depending  on if users have previously liked them.
    comments = Comment.objects.filter(post=post, reply=None).order_by('id')
    for comment in comments:
        comment.is_liked = False
        if comment.likes.filter(id=request.user.id).exists():
            comment.is_liked = True
        else:
            comment.is_liked = False
# For every user viewing the page the views field will be incremented by one.
    post.views += 1
    post.save()

# This method allows for the user to comment on the post using the commment
# form found in forms.py. If the user wishes to reply to a particular comment,
# a javascript feature will display a drop down of previous replies and a
# comment box.

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
# If there is a reply_id in the form this will trigger a query to get all
# replies to a particular comment.
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user,
                                             content=content, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {'post': post, 'comments': comments,
               'comment_form': comment_form,
               'total_upvotes': post.total_upvotes(),
               'is_upvoted': is_upvoted}

    return render(request, 'bugs/post_detail.html', context)


# This allows user to upvote or downvote post. User must be logged in to do so.
@login_required
def upvote_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
        is_upvoted = False
    else:
        post.upvotes.add(request.user)
        is_upvoted = True
    return HttpResponseRedirect(post.get_absolute_url())


# This allows user to like a comment. User must be logged in to do so.
@login_required
def like_comment(request):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
        is_liked = False
    else:
        comment.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(comment.get_absolute_url())


# This allows user to create a bug post if they are logged in. Even if they
# are not logged in the option will not show in the browser.
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
    context = {'form': form}
    return render(request, 'bugs/post_create.html', context)


# This option will only display when the user is the creator of the post.
# From this they will be update the details of the problem in response to
# comments if necessary.
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
    
    
        
    

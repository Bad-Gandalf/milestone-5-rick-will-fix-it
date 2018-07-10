from django.shortcuts import render

# Create your views here.
from __future__ import unicode_literals

from .models import Feature, Comment
from datetime import datetime
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def feature_list(request):
    features = Feature.objects.all().order_by('-created_date')
    context = {'features': features,}
    return render(request, 'features/post_list.html', context)
    
def feature_detail(request, pk, slug):
    feature = get_object_or_404(Feature, pk=pk, slug=slug)
    comments = Comment.objects.filter(feature=feature).order_by('-id')
    feature.views += 1
    feature.save()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(feature=feature, user=request.user, content=content)
            comment.save()
    
    else:
        comment_form = CommentForm()
            
    context = {'feature': feature, 'comments': comments, 'comment_form': comment_form,}
    return render(request, 'features/feature_detail.html', context)



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
    return render(request, 'features/post_create.html', context)
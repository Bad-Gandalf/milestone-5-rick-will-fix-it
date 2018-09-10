from __future__ import unicode_literals
from django.shortcuts import render
from .models import Feature, Comment
from django.db.models import Sum, Count
from datetime import datetime
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .view_functions import total_feature_contributions


def feature_list(request):
    """Retrieve list of features that are set to either open or working"""
    features = Feature.objects.exclude(status=1).exclude(status=4).annotate(comments=Count('comment', distinct=True))
    for feature in features:
        """total_feature_contributions() is a function that totals all the 
        contributions to that feature. It is defined in 
        features/view_functions.py"""
        feature.total_contributions = total_feature_contributions(feature)
    context = {'features': features,}
    return render(request, 'features/feature_list.html', context)
    

def feature_detail(request, id, slug):
    """Displays the detail page for specific feature and fetches the comments 
    for it. It further checks if each comment has been previously liked by the 
    user in order to change the option to unlike"""
    feature = get_object_or_404(Feature, pk=id, slug=slug)
    comments = Comment.objects.filter(feature=feature, reply=None).order_by('id')
    for comment in comments:
        comment.is_liked = False
        if comment.likes.filter(id=request.user.id).exists():
            comment.is_liked = True
        else:
            comment.is_liked = False
    total_contributions = total_feature_contributions(feature)
    feature.views += 1
    feature.save()
    """Allows user to comment on the feature. The option to comment will 
    not be there if user is not logged in."""
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            """Finds replies to a particular comment if user wished to reply to 
            that particular comment"""
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(feature=feature, user=request.user, content=content, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(feature.get_absolute_url())
    
    else:
        comment_form = CommentForm()
            
    context = {'feature': feature, 'comments': comments, 'comment_form': comment_form,
                'total_contributions': total_contributions, }
    return render(request, 'features/feature_detail.html', context)
    
    


@login_required    
def feature_create(request):
    """If user is logged in they can create a feature. There is form validation
    included. The option to create a feature will not display if the user is 
    not logged in"""
    if request.method == 'POST':
        form = FeatureCreateForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
            return HttpResponseRedirect(feature.get_absolute_url())
    else:
        form = FeatureCreateForm()
    context = {'form': form,}
    return render(request, 'features/feature_create.html', context)

    
    
@login_required
def like_feature_comment(request):
    """If user is logged in they can like a comment if they have not already.
    Conversely they can unlike the comment if they have previously liked it."""
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
        is_liked = False
    else:
        comment.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(comment.get_absolute_url())
from django.shortcuts import render

# Create your views here.
from __future__ import unicode_literals
from .models import Feature, Comment
from django.db.models import Sum
from datetime import datetime
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .view_functions import total_feature_contributions

# Create your views here.
def feature_list(request):
    features = Feature.objects.annotate(total_contributions=Sum('contributions__contribution')).order_by('-created_date')
    context = {'features': features,}
    return render(request, 'features/feature_list.html', context)
    
def feature_detail(request, pk, slug):
    feature = get_object_or_404(Feature, pk=pk, slug=slug)
    comments = Comment.objects.filter(feature=feature).order_by('-id')
    total_contributions = total_feature_contributions(feature)
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
            
    context = {'feature': feature, 'comments': comments, 'comment_form': comment_form,
                'total_contributions': total_contributions,
    }
    return render(request, 'features/feature_detail.html', context)



@login_required    
def feature_create(request):
    if request.method == 'POST':
        form = FeatureCreateForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
    else:
        form = FeatureCreateForm()
    context = {'form': form,}
    return render(request, 'features/feature_create.html', context)
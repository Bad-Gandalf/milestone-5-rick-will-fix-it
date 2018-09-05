from django.shortcuts import render
from blog.models import Blog
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    today = datetime.today()
    month = today - timedelta(days=31)
    blogs = list(Blog.objects.filter(published_date__gte=month).order_by('-published_date'))
    context = {"blogs":blogs}
    """Return the index.html file"""
    return render(request, 'blog/index.html', context)
    
    
def blog_detail(request, id, slug):
    blog = get_object_or_404(Blog, pk=id, slug=slug)
    context = {'blog': blog}
    blog.views += 1
    blog.save()
    return render(request, 'blog/blog_detail.html', context)
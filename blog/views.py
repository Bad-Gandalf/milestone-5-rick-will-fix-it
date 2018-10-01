from django.shortcuts import render
from blog.models import Blog
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta


# This is the view for the homepage. It includes the blog posts working as
# updates on either bugs or features for the site. It is currently set so only
# posts from the previous month will display.
def index(request):
    today = datetime.today()
    month = today - timedelta(days=31)
    blogs = list(Blog.objects.filter(published_date__gte=month)
                 .order_by('-published_date'))
    context = {"blogs": blogs}
    """Return the index.html file"""
    return render(request, 'blog/index.html', context)


# The detail view for a particular blog post.
def blog_detail(request, id, slug):
    blog = get_object_or_404(Blog, pk=id, slug=slug)
    context = {'blog': blog}
    blog.views += 1
    blog.save()
    return render(request, 'blog/blog_detail.html', context)
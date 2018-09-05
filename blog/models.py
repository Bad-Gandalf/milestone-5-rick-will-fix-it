from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from bugs.models import Post
from features.models import Feature
from django.utils import timezone
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User, related_name='blog_posts')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    bug = models.ForeignKey(Post, null=True, blank=True, related_name='bug_blog')
    feature = models.ForeignKey(Feature, null=True, blank=True, related_name='feature_blog')
    views = models.IntegerField(default=0)
   
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", args=[self.id, self.slug])
        
    
        
    
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from bugs.models import Post
from features.models import Feature
from django.utils import timezone
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save


# This model has optional foreign key fields for ugs and features if needed.
# If a site admin wishes to update on a particular bug or feature the link to
# that specific bug or feature will dispaly in the blog post detail page.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User, related_name='blog_posts')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    bug = models.ForeignKey(Post, null=True, blank=True,
                            related_name='bug_blog')
    feature = models.ForeignKey(Feature, null=True, blank=True,
                                related_name='feature_blog')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# Automatically create slug for model.
@receiver(pre_save, sender=Blog)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug
    print(kwargs)
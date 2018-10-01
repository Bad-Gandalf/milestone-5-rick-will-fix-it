from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):

    STATUS_CODES = ((1, _('Open')), (2, _('Working')), (3, _('Closed')))

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User, related_name='bug_posts')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    status = models.IntegerField(_('status'), default=1, choices=STATUS_CODES)
    upvotes = models.ManyToManyField(User, related_name="upvoted_posts")

    def __str__(self):
        return self.title
    
    
    # This method will count the users who have upvoted a bug post.
    def total_upvotes(self):
        return self.upvotes.count()

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id, self.slug])


# This automatically creates a slug for the post
@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug
    print(kwargs)


# This model is for comments on particular bug posts. It has a self-referential
# reply field to determine if the comment is a reply to another.
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment")
    user = models.ForeignKey(User)
    reply = models.ForeignKey('self', null=True, related_name="replies",
                              blank=True)
    content = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_post_comments")

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))
# This method will count the users who have liked a comment.

    def total_likes(self):
        return self.likes.count()
# This method directs to the url for the post.

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.post.id, self.post.slug])
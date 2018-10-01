from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.


class Feature(models.Model):
    """There are four status codes, the first will occur as the admins will 
    decide how much the feature will cost i.e. How much money needs to be 
    raised in order for work to begin. When price has been set the status will
    change to open. When contributions equal or exceed the price the status 
    will change to working."""
    STATUS_CODES = (
    (1, _('Awaiting Pricing')),
    (2, _('Open')),
    (3, _('Working')),
    (4, _('Closed')),
)

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User, related_name='feature')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    status = models.IntegerField(_('status'), default=1, choices=STATUS_CODES)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    
    def __str__(self):
        return self.title
        
        
    def get_absolute_url(self):
        return reverse("feature_detail", args=[self.id, self.slug])
        

@receiver(pre_save, sender=Feature)        
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug
    print(kwargs)
    
    
class Comment(models.Model):
    """"This model is for comments on aparticular feature. It has a self-referential
    reply field to determine if the comment is a reply to another.""" 
    feature = models.ForeignKey(Feature, related_name="comment")
    user = models.ForeignKey(User, related_name="user_feature_comment")
    reply = models.ForeignKey('self', null=True, related_name="replies", blank=True)
    content = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True,
                                   related_name="liked_feature_comments")
    
    def __str__(self):
        return '{}-{}'.format(self.feature.title, str(self.user.username))
        
    def total_likes(self):
        """This method counts the number of users who have liked a comment."""
        return self.likes.count()
        
    def get_absolute_url(self):
        return reverse("feature_detail", args=[self.feature.id, self.feature.slug])
        
    
from django.db import models
from bugs.models import Post
from django.contrib.auth.models import User

# Create your models here.
class PostWorkTime(models.Model):
    post = models.ForeignKey(Post)
    time_spent_mins = models.IntegerField(default=0)
    timestamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    
    
        
    
    def __str__(self):
        return '{}-{}-{}'.format(self.post.title, str(self.time_spent_mins), self.timestamp)
        
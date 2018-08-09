from django.db import models
from bugs.models import Post
from django.contrib.auth.models import User

# Create your models here.
class BugWorkTime(models.Model):
    bug = models.ForeignKey(Post)
    time_spent_mins = models.IntegerField(default=0)
    timestamp = models.DateField(auto_now_add=False)
    user = models.ForeignKey(User, null=True, blank=True)
    
    def __str__(self):
        return '{}-{}-{}'.format(self.bug.title, str(self.time_spent_mins), self.timestamp)
        
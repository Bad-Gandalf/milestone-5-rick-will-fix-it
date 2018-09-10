from django.db import models
from features.models import Feature, User

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

"""This model handles each contribution made to a feature"""        
class OrderLineItem(models.Model):
    user = models.ForeignKey(User, null=True, related_name="user_contribution")
    order = models.ForeignKey(Order, null=False, related_name="order_contribution")
    feature = models.ForeignKey(Feature, null=False, related_name='contributions')
    contribution = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.contribution, self.feature.title, self.user.username)
        
    
        
    
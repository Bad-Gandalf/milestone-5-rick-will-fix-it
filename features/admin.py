from django.contrib import admin
from .models import Feature, Comment
from checkout.models import OrderLineItem
from django.db import models
from django.db.models import Sum

# Register your models here.



class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'price', 'contributions')
    list_filter = ('status', 'created_date')
    search_fields = ('author__username', 'title')
    prepopulated_fields = {'slug' :('title',)}
    list_editable = ('status', 'price')
    date_hierarchy = ('created_date')
    
    def get_queryset(self, request):
        qs = super(FeatureAdmin, self).get_queryset(request)
        qs = qs.annotate(total_contributions=models.Sum('contributions__contribution'))
        return qs

    def contributions(self, obj):
        return obj.total_contributions
    
    contributions.admin_order_field = 'feature__contribution' 
    
        
    
        
    
        
    
    
    
    
admin.site.register(Comment)
admin.site.register(Feature, FeatureAdmin)
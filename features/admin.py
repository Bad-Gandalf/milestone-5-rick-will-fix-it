from django.contrib import admin
from .models import Feature, Comment
from django.db import models

# Register your models here.

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'price', 'amount_raised')
    list_filter = ('status', 'created_date')
    search_fields = ('author__username', 'title')
    prepopulated_fields = {'slug' :('title',)}
    list_editable = ('status', 'price')
    date_hierarchy = ('created_date')
    
    
    
    
admin.site.register(Comment)
admin.site.register(Feature, FeatureAdmin)
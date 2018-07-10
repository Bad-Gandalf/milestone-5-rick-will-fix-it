from django.contrib import admin
from .models import Post, Comment
from django.db import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'total_upvotes')
    list_filter = ('status', 'created_date')
    search_fields = ('author__username', 'title')
    prepopulated_fields = {'slug' :('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created_date')
    
    
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        qs = qs.annotate(models.Count('upvotes'))
        return qs

    def total_upvotes(self, obj):
        return obj.upvotes__count
    
    total_upvotes.admin_order_field = 'upvotes__count'
    
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
    
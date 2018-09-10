from django.contrib import admin
from .models import Post, Comment
from django.db import models

# The admin panel will display the posts in a manner that is easy to read.
# Admins can see the most popular/urgent bugs quickly depending on 
# total_upvotes. They can also adjust the status of the bug easily. 

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
    
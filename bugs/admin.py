from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created_date')
    search_fields = ('author__username', 'title')
    prepopulated_fields = {'slug' :('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created_date')
    

admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
    
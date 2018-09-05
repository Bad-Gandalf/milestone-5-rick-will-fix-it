from django.contrib import admin
from django.contrib.auth.models import User
from .models import Blog
from django.db import models

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author')
    list_filter = ('published_date', )
    search_fields = ('author__username', 'title')
    prepopulated_fields = {'slug' :('title',)}
    
    date_hierarchy = ('published_date')
    
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['author'].queryset = User.objects.filter(is_staff=True)
        return super(BlogAdmin, self).render_change_form(request, context, *args, **kwargs)
    

admin.site.register(Blog, BlogAdmin)
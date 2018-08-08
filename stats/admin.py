from django.contrib import admin
from .models import PostWorkTime
from bugs.models import Post
from django.contrib.auth.models import User


class PostWorkTimeAdmin(admin.ModelAdmin):
    
    list_display = ('post', 'timestamp', 'user', 'time_spent_mins', )
    date_hierarchy = ('timestamp')
    
    
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['post'].queryset = Post.objects.filter(status=2)
        context['adminform'].form.fields['user'].queryset = User.objects.filter(is_staff=True)
        return super(PostWorkTimeAdmin, self).render_change_form(request, context, *args, **kwargs)
    
    
    
admin.site.register(PostWorkTime, PostWorkTimeAdmin)

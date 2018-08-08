from django.contrib import admin
from .models import PostWorkTime
from bugs.models import Post


class PostWorkTimeAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['post'].queryset = Post.objects.filter(status=2)
        return super(PostWorkTimeAdmin, self).render_change_form(request, context, *args, **kwargs)
    
    
    
admin.site.register(PostWorkTime, PostWorkTimeAdmin)

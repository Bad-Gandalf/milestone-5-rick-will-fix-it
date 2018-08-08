from django.shortcuts import render
from bugs.models import Post

# Create your views here.
def record_time_spent_per_bug(request):
    bugs = Post.objects.filter(status=2)
    context = {"bugs": bugs,}
    return render(request, 'stats/record_time.html', context)
        
    
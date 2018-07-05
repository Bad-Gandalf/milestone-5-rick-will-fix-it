from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostCreateForm, UserLoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'bugs/post_list.html', context)
    
def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)
    
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/post_create.html', context)
    
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
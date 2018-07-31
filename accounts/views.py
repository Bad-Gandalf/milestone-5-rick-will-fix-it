from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.models import Profile

# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request, 'accounts/index.html')

@login_required    
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method =="POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else: 
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "accounts/login.html", {"login_form": login_form})
    
    
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'registration_form': registration_form})
    
def user_profile(request, id):
    """The user's profile page"""
    user = get_object_or_404(User, pk=request.user.id)
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'accounts/profile.html', {"profile": profile, "user": user})
    
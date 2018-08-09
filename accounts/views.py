from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileForm, UserForm
from accounts.models import Profile
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    """Return the index.html file"""
    try:
        return render(request, 'accounts/index.html')
    except Exception as e:
        print (e)
        return render(request, 'error.html')

@login_required    
def logout(request):
    """Log the user out"""
    try:
        auth.logout(request)
        messages.success(request, "You have successfully been logged out")
        return redirect(reverse('index'))
    
    except Exception as e:
        print (e)
        return render(request, 'error.html')
    
def login(request):
    """Return a login page"""
    try:
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
    
    except Exception as e:
        print (e)
        return render(request, 'error.html')
    
    
def registration(request):
    """Render the registration page"""
    try:
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
    
    except Exception as e:
        print (e)
        return render(request, 'error.html')
    
def user_profile(request, id):
    """The user's profile page"""
    try:
        user = get_object_or_404(User, pk=id)
        profile = get_object_or_404(Profile, user=id)
        return render(request, 'accounts/profile.html', { "profile": profile, "user":user})
    except Exception as e:
        print (e)
        return render(request, 'error.html')
   

@login_required    
def edit_profile(request, id):
    try:
        if request.method == "POST":
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile = profile_form.save()
                messages.success(request, 'Your profile was successfully updated!')
                return HttpResponseRedirect(profile.get_absolute_url())
            else:
                messages.error(request, 'Please correct the error below.')
            
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'accounts/edit_profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })
    
    except Exception as e:
        print (e)
        return render(request, 'error.html')
        
        

    
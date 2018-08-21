from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile
from django.contrib.admin import widgets


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""
    
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    email = forms.CharField(required=True, max_length=50, label='Email')
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets={
            'email': forms.EmailInput(attrs={'class': 'form-control', 'cols':'50'})
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
        
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("please confirm your password")
            
        if password1 != password2:
            raise ValidationError("Passwords must match")
            
        return password2
        
class ProfileForm(forms.ModelForm):
    bio = forms.CharField(label="Bio", widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ["date_of_birth", "location", "bio", "photo"]
        widget = {
            "date_of_birth" : forms.DateInput(attrs={'class': 'datepicker'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            
        }
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')



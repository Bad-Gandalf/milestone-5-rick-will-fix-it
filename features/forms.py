from django import forms
from .models import Feature, Comment

class FeatureCreateForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = (
            'title',
            'content',
            'image',)
            
class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        

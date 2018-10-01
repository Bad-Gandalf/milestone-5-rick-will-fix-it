from django import forms
from .models import Feature, Comment


class FeatureCreateForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = (
            'title',
            'content',
            'image',)
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'content': forms.Textarea(attrs={'class': 'form-control'})}


class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
                              'class': 'form-control',
                              'placeholder': 'Text goes here!!!',
                              'rows': '2', 'cols': '50'}))

    class Meta:
        model = Comment
        fields = ('content',)


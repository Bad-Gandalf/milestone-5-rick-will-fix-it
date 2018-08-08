from django import forms
from .models import PostWorkTime

class PostWorkTimeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PostWorkTimeForm, self).__init__(*args, **kwargs)
        self.fields['time_spent_mins'].widget.attrs['min'] = 1.00 
    
    class Meta:
        Model = PostWorkTime
        fields = ["time_spent_mins",]
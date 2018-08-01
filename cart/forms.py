from django import forms
from checkout.models import OrderLineItem

class ContributionForm(forms.ModelForm):
    class Meta:
        model = OrderLineItem
        fields = ['contribution',]
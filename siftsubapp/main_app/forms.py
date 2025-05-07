from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'cost', 'renewal_date', 'status', 'logo', 'uploaded_logo']
        widgets = {
            'renewal_date': forms.DateInput(attrs={'type': 'date'}),
        }

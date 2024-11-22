from django import forms
from .models import ConnectionRequest

class ConnectionRequestForm(forms.ModelForm):
    class Meta:
        model = ConnectionRequest
        fields = ['from_user', 'to_user']

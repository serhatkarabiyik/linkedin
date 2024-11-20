from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}))
    email = forms.CharField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']
        labels = {
            'last_name': "Nom",
            'first_name': "Prénom",
            'email': "Adresse e-mail",
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cette adresse e-mail est déjà utilisée.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Les mots de passe ne correspondent pas.")

        return cleaned_data
        


class ProfileUpdateForm(forms.ModelForm):
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}))
    email = forms.CharField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    picture = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lien de l\'image'}))

    class Meta:
        model = Profile
        fields = ['last_name', 'first_name', 'email', 'picture']
        labels = {
            'last_name': "Nom",
            'first_name': "Prénom",
            'email': "Adresse e-mail",
            'picture': 'Photo de profil',
        }
       


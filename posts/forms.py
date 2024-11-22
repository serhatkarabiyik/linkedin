from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Partagez une pensée...'
        }),
        required=True
    )
    picture = forms.URLField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Lien de l'image"})
    )

    class Meta:
        model = Post
        fields = ['content', 'picture']

from django import forms
from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'content', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.SelectDateWidget(years=range(1990, 2025)),
            'end_date': forms.SelectDateWidget(years=range(1990, 2025)),
        }

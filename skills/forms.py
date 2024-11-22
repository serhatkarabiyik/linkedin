from django import forms
from .models import Skill

class SkillForm(forms.Form):
    new_skill = forms.CharField(max_length=100, required=False, label="Nouvelle compétence")
    existing_skills = forms.ModelChoiceField(queryset=Skill.objects.all(), required=False, label="Compétence existante", empty_label="Sélectionner une compétence")

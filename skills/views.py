from django.shortcuts import render, redirect
from django.views import View
from .models import Skill
from .forms import SkillForm
from users.models import Profile

class SkillView(View):
    def get(self, request):
        skills = Skill.objects.all()
        profile = Profile.objects.get(user=request.user)
        profile_skills = profile.skills.all() 

        skill_form = SkillForm()

        return render(request, 'profile.html', {
            'skills': skills,
            'profile_skills': profile_skills,
            'skill_form': skill_form,
        })

    def post(self, request):
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill = skill_form.save()
            profile = Profile.objects.get(user=request.user)
            profile.skills.add(skill)

        return redirect('profile')

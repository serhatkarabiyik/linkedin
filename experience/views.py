from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Experience
from .forms import ExperienceForm
from django.http import Http404

class ExperienceView(View):
    def get(self, request):
        experiences = Experience.objects.filter(user=request.user)
        form = ExperienceForm()

        return render(request, 'profile.html', {
            'experiences': experiences,
            'form': form,
            'can_edit': True
        })

    def post(self, request):
        form = ExperienceForm(request.POST)

        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user 
            experience.save()
            return redirect('profile')

        return render(request, 'profile.html', {'form': form, 'can_edit': True})


class EditExperienceView(View):
    def get(self, request, pk=None):
        if pk:
            experience = get_object_or_404(Experience, pk=pk)
            if experience.user != request.user:
                raise Http404("Vous n'êtes pas autorisé à modifier cette expérience.")
        else:
            experience = None

        form = ExperienceForm(instance=experience)
        return render(request, 'profile.html', {'form': form, 'experience': experience})

    def post(self, request, pk=None):
        if pk:
            experience = get_object_or_404(Experience, pk=pk)
            if experience.user != request.user:
                raise Http404("Vous n'êtes pas autorisé à modifier cette expérience.")
        else:
            experience = None  

        form = ExperienceForm(request.POST, instance=experience)

        if form.is_valid():
            new_experience = form.save(commit=False)
            new_experience.user = request.user 
            new_experience.save()
            return redirect('profile')

        return render(request, 'profile.html', {'form': form, 'experience': experience})

class DeleteExperienceView(View):
    def post(self, request, pk):
        experience = get_object_or_404(Experience, pk=pk)

        if experience.user != request.user:
            raise Http404("Vous n'êtes pas autorisé à supprimer cette expérience.")

        experience.delete()
        return redirect('profile')

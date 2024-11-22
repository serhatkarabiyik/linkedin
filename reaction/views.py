from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Reaction
from posts.models import Post

class AddReactionView(LoginRequiredMixin, View):
    login_url = '/login/' 

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        
        reactions = post.reaction_set.all()

        reaction_counts = {
            'like': reactions.filter(reaction='like').count(),
            'bravo': reactions.filter(reaction='bravo').count(),
            'soutien': reactions.filter(reaction='soutien').count(),
            'j_adore': reactions.filter(reaction='j_adore').count(),
            'instructif': reactions.filter(reaction='instructif').count(),
            'drôle': reactions.filter(reaction='drôle').count(),
        }

        context = {
            'post': post,
            'reactions': reactions,
            'reaction_counts': reaction_counts,
        }

        return render(request, 'home', context)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        reaction_type = request.POST.get('reaction')

        if reaction_type not in dict(Reaction.REACTION_CHOICES).keys():
            return redirect('home')  

        reaction, created = Reaction.objects.update_or_create(
            user=request.user,
            post=post,
            defaults={'reaction': reaction_type}
        )

        return redirect('home')

    


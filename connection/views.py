from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Connection

class ConnectionRequestsView(LoginRequiredMixin, View):
    login_url = '/login/' 

    def get(self, request):
        received_requests = Connection.objects.filter(to_user=request.user, accepted=False)

        return render(request, 'connection_requests.html', {'received_requests': received_requests})

    def post(self, request, request_id):
        connection_request = get_object_or_404(Connection, id=request_id, to_user=request.user)

        action = request.POST.get('action')

        if action == 'accept':
            connection_request.accepted = True
            connection_request.save()
        elif action == 'reject':
            connection_request.delete()

        return redirect('connection_requests')

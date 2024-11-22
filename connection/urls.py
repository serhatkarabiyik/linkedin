from django.urls import path
from .views import ConnectionRequestsView

urlpatterns = [
    path('', ConnectionRequestsView.as_view(), name='connection_requests'),
]

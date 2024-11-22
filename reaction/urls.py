from django.urls import path
from . import views

urlpatterns = [
    path('reaction/<int:post_id>/', views.AddReactionView.as_view(), name='add_reaction'),
]

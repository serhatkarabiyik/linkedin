from django.urls import path
from .views import ExperienceView, EditExperienceView, DeleteExperienceView

urlpatterns = [
    path('', ExperienceView.as_view(), name='add_experience'),
    path('<int:pk>/', EditExperienceView.as_view(), name='edit_experience'),
    path('delete/<int:pk>/', DeleteExperienceView.as_view(), name='delete_experience'),
]

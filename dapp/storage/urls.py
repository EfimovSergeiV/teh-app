from django.urls import path
from storage.views import ProjectArchiveView

urlpatterns = [
    path('projects/', ProjectArchiveView.as_view()),
]


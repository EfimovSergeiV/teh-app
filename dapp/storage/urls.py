from django.urls import path

from storage.views import (
    GetOneProject,
    GetallProjectArchiveView,
    CreateOrUpdateView, 
    CreateProjectArchiveView, 
    AppendProjectArchiveView,
)


urlpatterns = [
    path('projects/getone/<int:pk>/', GetOneProject.as_view()),
    path('projects/getall/', GetallProjectArchiveView.as_view()),
    path('projects/create-or-update/', CreateOrUpdateView.as_view()),
    path('projects/create/', CreateProjectArchiveView.as_view()),
    path('projects/append/', AppendProjectArchiveView.as_view()),
]


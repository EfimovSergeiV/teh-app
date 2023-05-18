from django.urls import path

from storage.views import (
    GetOneProject,
    GetallProjectArchiveView,
    CreateOrUpdateProjectView,
    CreateOrUpdateFilesView,
    CreateProjectArchiveView, 
    AppendProjectArchiveView,
)


urlpatterns = [
    path('projects/getone/<int:pk>/', GetOneProject.as_view()),
    path('projects/getall/', GetallProjectArchiveView.as_view()),
    path('projects/create-or-update/', CreateOrUpdateProjectView.as_view()),
    path('files/create-or-update/', CreateOrUpdateFilesView.as_view()),
    path('projects/create/', CreateProjectArchiveView.as_view()),
    path('projects/append/', AppendProjectArchiveView.as_view()),
]


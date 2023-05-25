from django.urls import path

from storage.views import (
    CategoryView,
    GetOneProject,
    GetallProjectArchiveView,
    CreateOrUpdateProjectView,
    CreateOrUpdateFilesView,
    SearchView,
    # CreateProjectArchiveView, 
    # AppendProjectArchiveView,
)


urlpatterns = [
    path('cts/', CategoryView.as_view()),
    path('projects/getone/<int:pk>/', GetOneProject.as_view()),
    path('projects/<int:pk>/', GetallProjectArchiveView.as_view()),
    path('projects/create-or-update/', CreateOrUpdateProjectView.as_view()),
    path('projects/create-or-update/<int:pk>/', CreateOrUpdateProjectView.as_view()),
    path('files/create-or-update/', CreateOrUpdateFilesView.as_view()),
    path('search/', SearchView.as_view()),

    # path('projects/create/', CreateProjectArchiveView.as_view()),
    # path('projects/append/', AppendProjectArchiveView.as_view()),
]


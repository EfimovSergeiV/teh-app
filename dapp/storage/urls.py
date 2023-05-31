from django.urls import path

from storage.views import (
    CategoryView,
    GetOneProject,
    GetallProjectArchiveView,
    CreateOrUpdateProjectView,
    AssemblyView,
    CreateOrUpdateFilesView,
    SearchView,

    UploadLatestFileView,
    UpdateLatestFileView,

)


urlpatterns = [
    path('cts/', CategoryView.as_view()),
    path('projects/getone/<int:pk>/', GetOneProject.as_view()),
    path('projects/<int:pk>/', GetallProjectArchiveView.as_view()),
    path('projects/create-or-update/', CreateOrUpdateProjectView.as_view()),
    path('assembly/create/', AssemblyView.as_view()),
    # path('projects/update/<int:pk>/', CreateOrUpdateProjectView.as_view()),
    path('files/create-or-update/', CreateOrUpdateFilesView.as_view()),



    path('files/upload-latest-file/', UploadLatestFileView.as_view()),
    path('files/update-latest-file/<int:pk>/', UpdateLatestFileView.as_view()),
    

    path('search/', SearchView.as_view()),

    # path('projects/create/', CreateProjectArchiveView.as_view()),
    # path('projects/append/', AppendProjectArchiveView.as_view()),
]


from django.urls import path

from storage.views import (
    GetallProjectArchiveView, 
    CreateProjectArchiveView, 
    AppendProjectArchiveView,
)


urlpatterns = [
    path('projects/getall/', GetallProjectArchiveView.as_view()),
    path('projects/create/', CreateProjectArchiveView.as_view()),
    path('projects/append/', AppendProjectArchiveView.as_view()),
]


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from storage.models import ProjectArchiveModel
from storage.serializers import ProjectArchiveSerializer


class ProjectArchiveView(APIView):
    """ Представление файлов моделей """

    def get(self, request):

        qs = ProjectArchiveModel.objects.get(id=1)
        sr = ProjectArchiveSerializer(qs, context={'request':request})

        return Response(sr.data)
    
    def post(self, request):
        print(request.data)

        return Response({"status": 200})
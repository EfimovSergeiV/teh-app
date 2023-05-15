from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from storage.models import ProjectArchiveModel
from storage.serializers import ProjectArchiveSerializer
from django.core.files.storage import FileSystemStorage
import hashlib


class ProjectArchiveView(APIView):
    """ Представление файлов моделей """

    def get(self, request):

        qs = ProjectArchiveModel.objects.get(id=1)
        sr = ProjectArchiveSerializer(qs, context={'request':request})

        return Response(sr.data)
    
    def post(self, request):
        # print(request.data)

        file = request.data["file"]
        # print(f'{type(file)}:{file}')

        file = request.FILES['file']
        fs = FileSystemStorage()

        # Узнаём хэш сумму
        md5 = hashlib.md5()
        for chunk in file.chunks():
            md5.update(chunk)
        file_md5sum = md5.hexdigest()
        print(file_md5sum)
        

        fs.save(file.name, file)

        return Response({"status": 200})
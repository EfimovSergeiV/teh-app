from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from storage.models import ProjectArchiveModel
from storage.serializers import ProjectArchiveSerializer
from django.core.files.storage import FileSystemStorage
import hashlib, zipfile


def check_zip_password(file_path):
    try:
        with zipfile.ZipFile(file_path) as zip_file:
            # Получаем имена файлов в архиве
            file_names = zip_file.namelist()
            # Проверяем, защищен ли архив паролем
            if zip_file.comment:
                return True
            for file_name in file_names:
                # Получаем информацию о файле
                file_info = zip_file.getinfo(file_name)
                # Проверяем, защищен ли файл паролем
                if file_info.flag_bits & 0x1:
                    return True
        return False
    except zipfile.BadZipFile:
        # Если файл не является ZIP-архивом, возвращаем False
        return False


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


        if check_zip_password(file):
            print("обнаружен пароль на архиве")
            return Response({"status": "Не сохранено. На архиве обнаружен пароль"})


        else:
            # Узнаём хэш сумму
            md5 = hashlib.md5()
            for chunk in file.chunks():
                md5.update(chunk)
            file_md5sum = md5.hexdigest()
            print(file_md5sum)
            

            fs.save(file.name, file)

            return Response({"status": 200})
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from storage.models import ProjectArchiveModel
from storage.serializers import ProjectArchiveSerializer
from django.core.files.storage import FileSystemStorage
import hashlib, zipfile


def check_zip_password(file_path):
    """ Проверка на запароленный архив """
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
    
def get_md5_summ(file):
    """ Проверка MD5 суммы архива """
    md5 = hashlib.md5()
    for chunk in file.chunks():
        md5.update(chunk)
    file_md5sum = md5.hexdigest()
    return file_md5sum



class GetOneProject(APIView):
    """ Данные выбранного проекта """

    def get(self, request, pk):
        qs = ProjectArchiveModel.objects.get(id=pk)
        sr = ProjectArchiveSerializer(qs, context={'request': request})
        return Response(sr.data)



class GetallProjectArchiveView(APIView):
    """ Список всех проектов со всеми архивами """

    def get(self, request):

        qs = ProjectArchiveModel.objects.all()
        sr = ProjectArchiveSerializer(qs, many=True, context={'request':request})

        return Response(sr.data)
    


class CreateProjectArchiveView(APIView):
    """ Создаём проект и добавляем первый архив """

    def post(self, request):

        file = request.FILES['file']
        fs = FileSystemStorage()

        if check_zip_password(file):
            print("обнаружен пароль на архиве")
            return Response(data={'id': 1, 'msg': "Архивы с паролем запрещены", 'type': 'error'})

        else:
            # Узнаём хэш сумму
            md5 = hashlib.md5()
            for chunk in file.chunks():
                md5.update(chunk)
            file_md5sum = md5.hexdigest()
            file_md5sum = get_md5_summ()
            

            fs.save(file.name, file)

            return Response(data={'id': 1, 'msg': f'MD: {file_md5sum}', 'type': 'success'})
        

class AppendProjectArchiveView(APIView):
    """ Добавляем архив к проекту """

    def post(self, request):

        file = request.FILES['file']
        fs = FileSystemStorage()

        if check_zip_password(file):
            print("обнаружен пароль на архиве")
            return Response(data={'id': 1, 'msg': "Архивы с паролем запрещены", 'type': 'error'})


        else:
            # Узнаём хэш сумму
            md5 = hashlib.md5()
            for chunk in file.chunks():
                md5.update(chunk)
            file_md5sum = md5.hexdigest()
            print(file_md5sum)
            

            fs.save(file.name, file)

            return Response(data={'id': 1, 'msg': f'MD: {file_md5sum}', 'type': 'success'})
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from storage.models import ProjectArchiveModel, FileArchiveModel, FileHistoryModel
from storage.serializers import (
    ProjectArchiveSerializer,
    ProjectCreateSerializer,
    FileArchiveSerializer,
    FileHistorySerializer,
    SearchSerializer,
)   
from django.core.files.storage import FileSystemStorage
import hashlib, zipfile
from storage.documents import FileDocument
from django.db.models import Case, When
from elasticsearch_dsl import Q



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
        print(f'\n{ request.headers }')
        qs = ProjectArchiveModel.objects.all()
        sr = ProjectArchiveSerializer(qs, many=True, context={'request':request})

        return Response(sr.data)


class CreateOrUpdateProjectView(APIView):
    """ Создать или обновить архив проекта """

    def post(self, request, pk=None):
        if request.data["description"] is None:
            request.data["description"] = 'Нет описания'

        data = request.data
        sr = ProjectCreateSerializer(data=data)

        if sr.is_valid():
            if pk:
                msg = 'Проект обновлён'
                qs = ProjectArchiveModel.objects.get(id=pk)
                sr.update(qs, sr.data)
            else:
                msg = 'Проект создан'
                sr.save()
            return Response(data={'id': 1, 'msg': f'{ msg }', 'type': 'success'})
        
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
        


class CreateOrUpdateFilesView(APIView):
    """ Создать или обновить архив проекта """

    def post(self, request):
        file = request.FILES['file']
        fs = FileSystemStorage()

        print(file.name, request.data)

        # Проверки архива
        if check_zip_password(file):
            print("обнаружен пароль на архиве")
            return Response(data={'id': 1, 'msg': "Архивы с паролем запрещены", 'type': 'error'})
        md5_summ = get_md5_summ(file)


        serializer = FileArchiveSerializer
        
        project = ProjectArchiveModel.objects.get(id=int(request.data["project_id"]))

        history_serializer = FileHistorySerializer
        history = FileHistoryModel.objects.get(id=3)

        history = history_serializer(history)

        

        hd = history.data
        hd["created_date"] = timezone.now()
        print(hd)

        data = {
            "project": project.id,
            "md5": md5_summ,
            "file": file,
            "author": "Пользователь",
            # "historical_files": [hd,],
        }

        try:
            data['name'] = request.data["name"]
        except KeyError:
            pass

        
        if request.data["file_id"] == 'newfile':
            # print("создаём новую запись, добавляем файл / заносим в историю")
            serializer_data = serializer(data=data)
            if serializer_data.is_valid():
                print("SAVING")
                serializer_data.save()
            else:
                print(serializer_data.errors)

        else:
            qs = FileArchiveModel.objects.get(id=request.data["file_id"])
            data['name'] = qs.name

            # print(f'data: {data}, id: {qs.id}, qs: {qs}')

            serializer_data = serializer(data=data)
            if serializer_data.is_valid():
                print("UPDATE")
                serializer_data.update(instance=qs, validated_data=serializer_data.validated_data) 
                # print(f'обновляем запись { request.data["file_id"]} / заносим в историю')

            else:
                print(serializer_data.errors)

        return Response(data={'id': 1, 'msg': f'Архив загружен', 'type': 'success'})


class SearchView(APIView):
    serializer_class = SearchSerializer
    document_class = FileDocument

    def post(self, request):
        search_query = request.data['name']
        query = Q('multi_match', query=search_query,
                fields=[
                    'name',
                    'author',
                    # 'created_date',
                ], fuzziness='auto')

        search = self.document_class.search().query(query) #[0:30]
        response = search.execute()
        print(response)

        files = [file.id for file in response ]
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(files)])
        qs = FileHistoryModel.objects.filter(id__in=files).order_by(preserved)

        serializer = self.serializer_class(qs, many=True, context={'request':request})
        return Response(serializer.data)

"""
{
    "id": 161,
    "name": "Модели",
    "author": "Владимир Путин",
    "created_date": "15.10.2012 11:25:22"
}
"""






    


# Ниже не нужны

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
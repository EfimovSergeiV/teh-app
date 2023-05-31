from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from storage.models import *
from storage.serializers import (
    CategorySerializer,
    ProjectArchiveSerializer,
    AssemblySerializer,
    FileArchiveSerializer,
    FileHistorySerializer,
    SearchSerializer,
)   
from django.core.files.storage import FileSystemStorage
import hashlib, zipfile
from storage.documents import FileDocument
from django.db.models import Case, When
from elasticsearch_dsl import Q
from django.contrib.auth.models import User



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



class CategoryView(APIView):
    """ Категории проектов """
    
    def get(self, request):
        qs = CategoryModel.objects.all()
        sr = CategorySerializer(qs, many=True, context={'request': request})
        return Response(sr.data)



class GetOneProject(APIView):
    """ Данные выбранного проекта """

    def get(self, request, pk):
        qs = ProjectArchiveModel.objects.get(id=pk)
        sr = ProjectArchiveSerializer(qs, context={'request': request})
        return Response(sr.data)



class GetallProjectArchiveView(APIView):
    """ Список всех проектов со всеми архивами """

    def get(self, request, pk):
        qs = ProjectArchiveModel.objects.filter(category_id=pk)
        sr = ProjectArchiveSerializer(qs, many=True, context={'request':request})
        return Response(sr.data)





class CreateOrUpdateProjectView(APIView):
    """ Создать или обновить архив проекта """
    pass
    def post(self, request):
        data = request.data
        if data["description"] is None:
            data["description"] = 'Нет описания'

        serializer = ProjectArchiveSerializer(data=data)

        if serializer.is_valid():
            if 'project' in data.keys():
                msg = 'Проект обновлён'
                print('update')
                project = ProjectArchiveModel.objects.get(id=data['project'])
                serializer.update(project, validated_data=serializer.validated_data)
            else:
                msg = 'Проект создан'
                serializer.save()

        return Response(data={'id': 1, 'msg': f'{ msg }', 'type': 'success'})
    

class AssemblyView(APIView):

    def post(self, request):

        data = request.data

        serializer = AssemblySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
            return Response(data={'id': 1, 'msg': f'Нада название сборки', 'type': 'error'})


        return Response(data={'id': 1, 'msg': f'Cборка добавлена', 'type': 'success'})

        


def add_file_to_history(data):
    """ Добавляем загруженный файл в историю """
    # Добавить обновление архива
    try:
        FileHistoryModel.objects.create(
            latest_id = data.id,
            author = data.author,
            created_date = data.created_date,
            name = data.name,
            md5 = data.md5,
            file = data.file,
        )
    except AttributeError:
        FileHistoryModel.objects.create(
            latest_id = data["id"],
            author = data["author"],
            created_date = data["created_date"],
            name = data["name"],
            md5 = data["md5"],
            file = data["file"],
        )



class CreateOrUpdateFilesView(APIView):
    """ Создать или обновить архив проекта """

    def post(self, request):
        file = request.FILES['file']
        fs = FileSystemStorage()

        # print(file.name, request.data)

        # Проверки архива
        if check_zip_password(file):
            print("обнаружен пароль на архиве")
            return Response(data={'id': 1, 'msg': "Архивы с паролем запрещены", 'type': 'error'})
        md5_summ = get_md5_summ(file)


        serializer = FileArchiveSerializer
        project = ProjectArchiveModel.objects.get(id=int(request.data["project_id"]))


        profile = User.objects.get(username=request.user)
        uploader = f'{profile.first_name} {profile.last_name}'
        author = request.data['author_history'] if 'author_history' in request.data.keys() else uploader
        created_data = datetime.fromisoformat(request.data['date_history']) if 'date_history' in request.data.keys() else timezone.now()


        data = {
            "project": project.id,
            "md5": md5_summ,
            "file": file,
            "author": author,
            "created_date": created_data
        }


        try:
            data['name'] = request.data["name"]
        except KeyError:
            pass


        #if 'date_history' not in request.data.keys():
        if request.data["file_id"] == 'newfile':
            # print("создаём новую запись, добавляем файл / заносим в историю")
            serializer_data = serializer(data=data)

            if serializer_data.is_valid():
                print("SAVING")
                saved_data = serializer_data.save()
            else:
                print(serializer_data.errors)


        else:
            qs = FileArchiveModel.objects.get(id=request.data["file_id"])
            data['name'] = qs.name

            # print(f'data: {data}, id: {qs.id}, qs: {qs}')

            serializer_data = serializer(data=data)
            if serializer_data.is_valid():
                print("UPDATE")
                if 'date_history' in request.data.keys():
                    print('move file to history')
                    saved_data = data
                    saved_data['id'] = int(request.data["file_id"])

                # print(f'обновляем запись { request.data["file_id"]} / заносим в историю')
                else:
                    print('move file to NOW')
                    saved_data = serializer_data.update(instance=qs, validated_data=serializer_data.validated_data) 

            else:
                print(serializer_data.errors)


        # Добавляем файл в историю загрузок
        print(saved_data)
        add_file_to_history(saved_data)
        return Response(data={'id': 1, 'msg': f'Архив загружен', 'type': 'success'})



# PRODUCTION

def add_file_to_history(data):
    """ Добавляем загруженный файл в историю """

    serializer = FileHistorySerializer(data=data)

    if serializer.is_valid():
        qs = serializer.save()
        return qs
    else:
        print(f'ERR HISTORY: {serializer.errors}')


class UploadLatestFileView(APIView):
    """ 
        Выгрузка архива, который будет отображаться как последний 
        и занесение его в историю версий файлов
    """

    def post(self, request):
        file = request.FILES['file']
        md5_summ = get_md5_summ(file)

        serializer = FileArchiveSerializer
        project = ProjectArchiveModel.objects.get(id=int(request.data["project_id"]))

        profile = User.objects.get(username=request.user)
        uploader = f'{profile.first_name} {profile.last_name}'
        author = request.data['author_history'] if 'author_history' in request.data.keys() else uploader
        created_data = datetime.fromisoformat(request.data['date_history']) if 'date_history' in request.data.keys() else timezone.now()

        data = {
            "project": project.id,
            "assembly": request.data["assembly_id"],
            "name": request.data["name"],
            "md5": md5_summ,
            "author": author,
            "created_date": created_data
        }

        serializer_data = serializer(data=data)        

        if serializer_data.is_valid():
            saved_data =  serializer_data.save()
            data["latest"] = saved_data.id

        else:
            print(f'ERR ARCHIVE: {serializer.errors}')
        
        data['file'] = file
        # Добавить этот файл в историю версий

        qs = add_file_to_history(data=data)
        latest = FileArchiveModel.objects.filter(id=saved_data.id)
        latest.update(file=str(qs.file))

        return Response(data={'id': 1, 'msg': f'Архив загружен', 'type': 'success'})

class UpdateLatestFileView(APIView):
    """ 
        Обновление архива, который будет отображаться как последний 
        и занесение его в историю версий файлов

        Сохранить файл в историю и обновить запись по последнем
    """

    def post(self, request, pk):
        file = request.FILES['file']
        md5_summ = get_md5_summ(file)

        serializer = FileArchiveSerializer
        project = ProjectArchiveModel.objects.get(id=int(request.data["project_id"]))

        profile = User.objects.get(username=request.user)
        uploader = f'{profile.first_name} {profile.last_name}'
        author = request.data['author_history'] if 'author_history' in request.data.keys() else uploader
        created_data = datetime.fromisoformat(request.data['date_history']) if 'date_history' in request.data.keys() else timezone.now()

        data = {
            "project": project.id,
            "assembly": request.data["assembly_id"],
            "name": request.data["name"],
            "md5": md5_summ,
            "author": author,
            "created_date": created_data
        }

        serializer_data = serializer(data=data)        

        if serializer_data.is_valid():
            print('VALIDED')
            # saved_data =  serializer_data.save()
            # data["latest"] = saved_data.id

        else:
            print(f'ERR ARCHIVE: {serializer.errors}')
        
        # data['file'] = file
        # # Добавить этот файл в историю версий

        # qs = add_file_to_history(data=data)
        # latest = FileArchiveModel.objects.filter(id=saved_data.id)
        # latest.update(file=str(qs.file))

        # return Response(data={'id': 1, 'msg': f'Архив загружен', 'type': 'success'})

        return Response(status=status.HTTP_200_OK)









class UnbuilderProjectView(APIView):
    """ Попробывать реализовать unbuilder, что бы загружать и раскладывать проект целиком, а не по одному архиву """
    def post(self, request):
        print(request.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)





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




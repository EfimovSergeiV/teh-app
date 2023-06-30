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
from storage.documents import FileDocument, InsertedFilesDocument
from django.db.models import Case, When
from elasticsearch_dsl import Q
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny ,IsAuthenticated, IsAuthenticatedOrReadOnly


    
def get_md5_summ(file):
    """ Проверка MD5 суммы архива """
    md5 = hashlib.md5()
    for chunk in file.chunks():
        md5.update(chunk)
    file_md5sum = md5.hexdigest()
    return file_md5sum



class CategoryView(APIView):
    """ Категории проектов """

    # permission_classes = [IsAuthenticatedOrReadOnly]
    
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
    




# PRODUCTION
class GetAssemblyView(APIView):
    def get(self, request, pk):
        qs = AssemblyModel.objects.filter(project_id=pk)
        serializer = AssemblySerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)

class GetLatestView(APIView):
    def get(self, request, pk):
        qs = FileArchiveModel.objects.filter(assembly_id=pk)
        serializer = FileArchiveSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)

class GetHistoryView(APIView):
    def get(self, request, pk):
        qs = FileHistoryModel.objects.filter(latest_id=pk)
        serializer = FileHistorySerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)






def add_file_to_history(data):
    """ Добавляем загруженный файл в историю """

    serializer = FileHistorySerializer(data=data)

    if serializer.is_valid():
        qs = serializer.save()
        return qs
    else:
        print(f'ERR HISTORY: {serializer.errors}')


def add_inserted_files(qs, file):
    """ Заполняем файлы, которые находятся в ахиве """

    with zipfile.ZipFile(file, 'r') as zip_file:
        files = zip_file.namelist()
        for file_name in files:
            InsertedFilesModel.objects.create(
                archive = qs,
                name = file_name,
                extension = 'file'
                )   



from transliterate import slugify
def rename_archive(filename):

    # project, assembly = str(instance.project.name), str(instance.assembly.name)
    # project_translate, assembly_translate = slugify(project), slugify(assembly)

    # project_path = project_translate if project_translate else project.replace(' ', '-').lower()
    # assembly_path = assembly_translate if assembly_translate else assembly.replace(' ', '-').lower()

    # print(f'Path: {project_path}/{assembly_path}/{filename}')
    return filename


class UploadLatestFileView(APIView):
    """ 
        Выгрузка архива, который будет отображаться как последний 
        и занесение его в историю версий файлов
    """

    def post(self, request):
        try:
            file = request.FILES['file']
            md5_summ = get_md5_summ(file)

            print(file.name)

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



        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer_data = FileArchiveSerializer(data=data)      

        if serializer_data.is_valid():
            print(f'ser valid {serializer_data.validated_data}')
            saved_data = serializer_data.save()
            data["latest"] = saved_data.id

        else:
            print(f'ERR ARCHIVE: {serializer_data.errors}')
        
        data['file'] = file

        qs = add_file_to_history(data=data)
        add_inserted_files(qs, file)

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

        try:
            file = request.FILES['file']
            md5_summ = get_md5_summ(file)
            
            latest_file = FileArchiveModel.objects.get(id=pk)

            profile = User.objects.get(username=request.user)
            uploader = f'{profile.first_name} {profile.last_name}'
            author = request.data['author_history'] if 'author_history' in request.data.keys() else uploader
            created_date = datetime.fromisoformat(request.data['date_history']) if 'date_history' in request.data.keys() else timezone.now()

            data = {
                "project": latest_file.project.id,
                "assembly": latest_file.assembly.id,
                "latest": latest_file.id,
                "name": request.data['file_name'],
                "md5": md5_summ,
                "author": author,
                "file": file,
                "created_date": created_date
            }

        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer_data = FileHistorySerializer(data=data)

        if serializer_data.is_valid():
            created = serializer_data.save()
            add_inserted_files(qs=created, file=file)
            FileArchiveModel.objects.filter(id=pk).update(
                md5 = md5_summ,
                author = author,
                name = data['name'],
                file = created.file,
                created_date = created_date
            )
            return Response(data={'id': 1, 'msg': f'Архив загружен', 'type': 'success'})

        else:
            print(f'ERR : {serializer_data.errors}')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
class CreateHistoryFileView(APIView):
    """ 
        Обновление архива, который будет отображаться как последний 
        и занесение его в историю версий файлов

        Сохранить файл в историю и обновить запись по последнем
    """

    def post(self, request, pk):
        try:
            file = request.FILES['file']
            md5_summ = get_md5_summ(file)
            latest_file = FileArchiveModel.objects.get(id=pk)
            profile = User.objects.get(username=request.user)
            uploader = f'{profile.first_name} {profile.last_name}'
            author = request.data['author_history'] if 'author_history' in request.data.keys() else uploader
            created_date = datetime.fromisoformat(request.data['date_history']) if 'date_history' in request.data.keys() else timezone.now()

            data = {
                "project": latest_file.project.id,
                "assembly": latest_file.assembly.id,
                "latest": latest_file.id,
                "name": request.data['name'],
                "md5": md5_summ,
                "author": author,
                "file": file,
                "created_date": created_date
            }
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer_data = FileHistorySerializer(data=data)

        if serializer_data.is_valid():
            qs = serializer_data.save()
            add_inserted_files(qs=qs, file=file)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data={'id': 1, 'msg': f'Архив загружен', 'type': 'success'})





import os, zipfile, shutil
from django.conf import settings
from pathlib import Path

def custom_builder(project, user, data):
    print(project, user, data)

    assembly_ids = data['assembly_ids']
    latest_ids = data['latest_ids']
    archive_ids = data['archive_ids']

    assemblys_qs = AssemblyModel.objects.filter(id__in=assembly_ids)
    latests_qs = FileArchiveModel.objects.filter(id__in=latest_ids)
    archives_qs = FileHistoryModel.objects.filter(id__in=archive_ids)

    path_to_files = f'{settings.BASE_DIR}/files/{user}/tmp/{project.name}/'
    path_to_zip = f'{settings.BASE_DIR}/files/{user}/{project.name}-build.zip'

    print("\nAssembly:")
    for assembly_qs in assemblys_qs:
        files = assembly_qs.assembly_files.all()
        
        if len(files) == 1:
            path_archive = f'{settings.BASE_DIR}/files/{files[0].file}'
            path_unpacking = f'{settings.BASE_DIR}/files/{user}/tmp/{project.name}/{assembly_qs.name}/'
            Path(path_unpacking).mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(path_archive, 'r') as zip_file:
                zip_file.extractall(path_unpacking)
        elif len(files) > 1:
            for file_qs in files:
                path_archive = f'{settings.BASE_DIR}/files/{file_qs.file}'
                path_unpacking = f'{settings.BASE_DIR}/files/{user}/tmp/{project.name}/{assembly_qs.name}/{file_qs.name}/'
                Path(path_unpacking).mkdir(parents=True, exist_ok=True)
                with zipfile.ZipFile(path_archive, 'r') as zip_file:
                    zip_file.extractall(path_unpacking)

    for latest_qs in latests_qs:
        path_archive = f'{settings.BASE_DIR}/files/{latest_qs.file}'
        path_unpacking = f'{settings.BASE_DIR}/files/{user}/tmp/{project.name}/{latest_qs.assembly}/{latest_qs.name}'
        Path(path_unpacking).mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(path_archive, 'r') as zip_file:
            zip_file.extractall(path_unpacking)

    for archive_qs in archives_qs:
        path_archive = f'{settings.BASE_DIR}/files/{archive_qs.file}'
        path_unpacking = f'{settings.BASE_DIR}/files/{user}/tmp/{project.name}/{archive_qs.assembly}/{archive_qs.name}_{archive_qs.created_date.strftime("%Y-%m-%d %H:%M:%S")}'
        Path(path_unpacking).mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(path_archive, 'r') as zip_file:
            zip_file.extractall(path_unpacking)

    # Бежим по директория и пакуем в архив
    archive_zip = zipfile.ZipFile(f'{path_to_zip}', 'w')
    for folder, subfolders, files in os.walk(f'{path_to_files}'):
        for file in files:
            archive_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), f'{path_to_files}'), compress_type = zipfile.ZIP_DEFLATED)
    archive_zip.close()

    url_to_zip = f'/files/{user}/{project.name}-build.zip'
    shutil.rmtree(f'{settings.BASE_DIR}/files/{user}/tmp/')
    return url_to_zip



class BuilderProjectView(APIView):
    """ Попробывать реализовать unbuilder, что бы загружать и раскладывать проект целиком, а не по одному архиву """

    def post(self, request, pk):
        user = request.user
        path = f'{settings.BASE_DIR}/files/{ user }/tmp/'

        print(request.data)

        project_qs = ProjectArchiveModel.objects.get(id=pk)
        assemplys_qs = project_qs.project_assembly.all()

        try:
            if len(request.data['assembly_ids']) > 0 or len(request.data['latest_ids']) > 0 or len(request.data['archive_ids']) > 0:
                build_url = custom_builder(project=project_qs, user=request.user, data=request.data)
                
                
                return Response({'file': f'http://192.168.60.201:8080{build_url}'})
        except KeyError:
            pass


        count = 0
        for assemply_qs in assemplys_qs:
            count += 1

            # ПОСЛЕДНЯЯ ВЕРСИЯ ФАЙЛОВ
            # Создаём директории если файл один, бросаем в корень, иначе доздаём вложенную директорию
            files = assemply_qs.assembly_files.all()
            if len(files) == 1:
                create_path = f'{path}{assemply_qs.name}'
                Path(create_path).mkdir(parents=True, exist_ok=True)
                zip_path = f'{ settings.BASE_DIR }/files/{files[0].file}'
                with zipfile.ZipFile(zip_path, 'r') as zip_file:
                    zip_file.extractall(create_path)

                print(f"Кидаем в корень: {create_path}")

            elif len(files) > 1:
                for file in files:
                    create_path = f'{path}{assemply_qs.name}/{file.name}'
                    Path(create_path).mkdir(parents=True, exist_ok=True)
                    zip_path = f'{ settings.BASE_DIR }/files/{file.file}'
                    with zipfile.ZipFile(zip_path, 'r') as zip_file:
                        zip_file.extractall(create_path)

                    print(f'Создаём вложенные директории: { create_path }')

        archive_zip = zipfile.ZipFile(f'{settings.BASE_DIR}/files/{user}/{project_qs.name}-build.zip', 'w')
        for folder, subfolders, files in os.walk(f'{settings.BASE_DIR}/files/{user}/tmp/'):
            for file in files:
                archive_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), f'{settings.BASE_DIR}/files/{user}/tmp/'), compress_type = zipfile.ZIP_DEFLATED)
        archive_zip.close()
        shutil.rmtree(f'{settings.BASE_DIR}/files/{user}/tmp/')

        return Response({'file': f'http://192.168.60.201:8080/files/{user}/{ project_qs.name }-build.zip'})




import psutil
class GetDiskSpaceView(APIView):
    """ Место на диске """
    
    def get(self, request):
        # Получаем информацию о диске, на котором находится текущая директория
        disk_usage = psutil.disk_usage('/')
        total_space = disk_usage.total / (1024 * 1024 * 1024)
        used_space = disk_usage.used / (1024 * 1024 * 1024)
        
        return Response({ "total_space": float(f"{total_space:.2f}"), 'used_space': float(f"{used_space:.2f}") })


class SearchView(APIView):
    serializer_class = SearchSerializer
    archive_document_class = FileDocument
    file_document_class = InsertedFilesDocument

    def get(self, request):
        """ Возвращает список всех авторов и крайние даты """

        archives_qs = FileHistoryModel.objects.all()
        authors = []
        extensions = []

        for archive_qs in archives_qs:
            if archive_qs.author not in authors:
                authors.append(archive_qs.author)

        return Response({
            "authors": authors,
            "extensions": extensions,
            "first_date": "",
            "latest_date": "",
        })


    def post(self, request):
        search_query = request.data['name']
        target = request.data['target']

        query = Q('multi_match', query=search_query,
                fields=[
                    'name',
                ], fuzziness='auto')


        if target == 'file':
            search = self.file_document_class.search().query(query)
            response = search.execute()
            ids = [file.id for file in response ]
            files = []
            response = InsertedFilesModel.objects.filter(id__in=ids)
            for inserted_qs in response:
                if inserted_qs.archive_id not in files:
                    files.append(inserted_qs.archive_id)

        else:
            search = self.archive_document_class.search().query(query)
            response = search.execute()
            files = [file.id for file in response ]

        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(files)])

        start_date = datetime.fromisoformat(request.data['start_date'])
        end_date = datetime.fromisoformat(request.data['end_date'])
        author = request.data['author']

        qs = FileHistoryModel.objects.filter(id__in=files).order_by(preserved)

        if author and author != 'null':
            qs = qs.filter(author=author)

        if start_date and end_date and start_date != 'null' and end_date != 'null':
            qs = qs.filter(created_date__range=(start_date, end_date))

        serializer = self.serializer_class(qs, many=True, context={'request':request})

        return Response(serializer.data)




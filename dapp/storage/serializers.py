from rest_framework import serializers
from storage.models import *


class CategorySerializer(serializers.ModelSerializer):
    """ категории проектов """

    class Meta:
        model = CategoryModel
        fields = '__all__'




class FileHistorySerializer(serializers.ModelSerializer):
    """ Сериалихзатор истории файла """

    class Meta:
        model = FileHistoryModel
        fields = '__all__'



class FileArchiveSerializer(serializers.ModelSerializer):
    """ Файлы """
    # historical_files = FileHistorySerializer(many=True, read_only=True)

    class Meta:
        model = FileArchiveModel
        fields = '__all__'
        


class AssemblySerializer(serializers.ModelSerializer):
    """ Узлы/сборки проекта """
    # assembly_files = FileArchiveSerializer(many=True, read_only=True)

    class Meta:
        model = AssemblyModel
        fields = '__all__'        


# class ProjectCreateSerializer(serializers.ModelSerializer):
#     """ Сериализатор представления моделей """
    
#     class Meta:
#         model = ProjectArchiveModel
#         fields = '__all__'


class ProjectArchiveSerializer(serializers.ModelSerializer):
    """ Сериализатор представления моделей """
    # project_files = FileArchiveSerializer(many=True, read_only=True)
    project_assembly = AssemblySerializer(many=True, read_only=True)
    
    class Meta:
        model = ProjectArchiveModel
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    """ Поиск по истории файлов """

    class Meta:
        model = FileHistoryModel
        fields = (
            'id', 
            'name',
            'author',
            'created_date',
            )
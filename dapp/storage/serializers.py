from rest_framework import serializers
from storage.models import ProjectArchiveModel, FileArchiveModel


class FileArchiveSerializer(serializers.ModelSerializer):
    """ Файлы """

    class Meta:
        model = FileArchiveModel
        fields = '__all__'


class ProjectCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор представления моделей """
    
    class Meta:
        model = ProjectArchiveModel
        fields = '__all__'

class ProjectArchiveSerializer(serializers.ModelSerializer):
    """ Сериализатор представления моделей """

    project_files = FileArchiveSerializer(many=True)
    
    class Meta:
        model = ProjectArchiveModel
        fields = '__all__'
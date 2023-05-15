from rest_framework import serializers
from storage.models import ProjectArchiveModel, FileArchiveModel


class FileArchiveSerializer(serializers.ModelSerializer):
    """ Файлы """

    class Meta:
        model = FileArchiveModel
        fields = '__all__'


class ProjectArchiveSerializer(serializers.ModelSerializer):
    """ Сериализатор представления моделей """

    project_file = FileArchiveSerializer(many=True)
    
    class Meta:
        model = ProjectArchiveModel
        fields = '__all__'
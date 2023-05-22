from rest_framework import serializers
from storage.models import ProjectArchiveModel, FileArchiveModel, FileHistoryModel


class FileHistorySerializer(serializers.ModelSerializer):
    """ Сериалихзатор истории файла """

    class Meta:
        model = FileHistoryModel
        fields = '__all__'



class FileArchiveSerializer(serializers.ModelSerializer):
    """ Файлы """
    historical_files = FileHistorySerializer(many=True)


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



from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from storage.models import FileHistoryModel, InsertedFilesModel


@registry.register_document
class FileDocument(Document):
    """ Elastic Search - архив """

    class Index:
        name = 'files'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = FileHistoryModel
        fields = [
            'id',
            'name',
        ]


@registry.register_document
class InsertedFilesDocument(Document):
    """ Elastic Search - файлы """

    class Index:
        name = 'inserted'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = InsertedFilesModel
        fields = [
            'id',
            'name',
        ]
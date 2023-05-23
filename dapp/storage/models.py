from django.db import models
from django.utils import timezone
import os


class ProjectArchiveModel(models.Model):
    """ Модели архивы """

    name = models.CharField(verbose_name="Название", max_length=120)
    description = models.TextField(verbose_name="Описание", max_length=5000, null=True, blank=True, default="Не описано")
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)
    updated_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['-updated_date',]

    def __str__(self) -> str:
        return self.name
    

def upload_file_to(instance, filename):
    related_model_id = instance.project_id
    directory_path = f"storage/models/{related_model_id}/"
    file_path = os.path.join(directory_path, filename)
    return file_path


class FileArchiveModel(models.Model):
    """ Файлы """
    
    project = models.ForeignKey(ProjectArchiveModel, verbose_name="Проект", related_name='project_files', on_delete=models.CASCADE)
    author = models.CharField(verbose_name="Автор", max_length=250)
    name = models.CharField(verbose_name="Название", max_length=250)
    md5 = models.CharField(verbose_name="MD5 сумма",max_length=100, null=True, blank=True)
    file = models.FileField(verbose_name="Архив", upload_to=upload_file_to)
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now=True)

    class Meta:
        verbose_name = "Архив"
        verbose_name_plural = "Архивы"
        ordering = ['-created_date',]


    def __str__(self) -> str:
        return f"{self.project.name} - { self.name }"
    

class FileHistoryModel(models.Model):
    """ История файлов """

    latest = models.ForeignKey(FileArchiveModel, related_name='historical_files', on_delete=models.CASCADE)
    author = models.CharField(verbose_name="Автор", max_length=250)
    name = models.CharField(verbose_name="Название", max_length=250)
    md5 = models.CharField(verbose_name="MD5 сумма",max_length=100, null=True, blank=True)
    file = models.CharField(verbose_name="Путь к архиву", max_length=500)
    created_date = models.DateTimeField(verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        ordering = ['-created_date',]

    def __str__(self) -> str:
        return self.name
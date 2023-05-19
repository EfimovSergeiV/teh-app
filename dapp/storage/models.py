from django.db import models
from django.utils import timezone
import os


class ProjectArchiveModel(models.Model):
    """ Модели архивы """

    name = models.CharField(verbose_name="Название", max_length=120)
    description = models.TextField(verbose_name="Описание", max_length=5000, null=True, blank=True, default="Не описано")
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"
        ordering = ['-id',]

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
    name = models.CharField(verbose_name="Название", max_length=250)
    md5 = models.CharField(verbose_name="MD5 сумма",max_length=100, null=True, blank=True)
    file = models.FileField(verbose_name="Архив", upload_to=upload_file_to)
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    history = models.JSONField(verbose_name="История изменений", null=True, blank=True)

    class Meta:
        verbose_name = "Архив"
        verbose_name_plural = "Архивы"


    def __str__(self) -> str:
        return self.file.name
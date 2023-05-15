from django.db import models
from django.utils import timezone


class ProjectArchiveModel(models.Model):
    """ Модели архивы """

    name = models.CharField(verbose_name="Название", max_length=120)
    description = models.TextField(verbose_name="Описание", max_length=5000,default="Не описано")
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self) -> str:
        return self.name
    

class FileArchiveModel(models.Model):
    """ Файлы """

    project = models.ForeignKey(ProjectArchiveModel, verbose_name="Проект", related_name='project_file', on_delete=models.CASCADE)
    md5 = models.CharField(verbose_name="MD5 сумма",max_length=100, null=True, blank=True)
    file = models.FileField(verbose_name="Архив", upload_to="img/c/doc/")
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)

    class Meta:
        verbose_name = "Архив"
        verbose_name_plural = "Архивы"

    def __str__(self) -> str:
        return self.file.name
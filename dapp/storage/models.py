from django.db import models
from django.utils import timezone
import os


class CategoryModel(models.Model):
    """ Категории проектов """
    name = models.CharField(verbose_name="Название категории", max_length=250)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "1. Категория"
        ordering = ['id',]

    def __str__(self) -> str:
        return self.name


class ProjectArchiveModel(models.Model):
    """ Модели архивы """

    category = models.ForeignKey(CategoryModel, verbose_name="Категория", related_name="project_category", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=120)
    description = models.TextField(verbose_name="Описание", max_length=5000, null=True, blank=True, default="Не описано")
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)
    updated_date = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "2. Проекты"
        ordering = ['-updated_date',]

    def __str__(self) -> str:
        return self.name


class AssemblyModel(models.Model):
    """ Узлы/сборки проекта """

    project = models.ForeignKey(ProjectArchiveModel, verbose_name="Проект", related_name='project_assembly', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название узла", max_length=250)

    class Meta:
        verbose_name = "Узел/Сборка"
        verbose_name_plural = "3. Узлы/Сборки"

    def __str__(self) -> str:
        return self.name


class FileArchiveModel(models.Model):
    """ Файлы ( не содержит самих файлов, а указывает, который является последним )"""
    
    project = models.ForeignKey(ProjectArchiveModel, verbose_name="Проект", related_name='project_files', on_delete=models.CASCADE)
    assembly = models.ForeignKey(AssemblyModel, verbose_name="Узел/Сборка", related_name='assembly_files', null=True, blank=True, on_delete=models.CASCADE)
    author = models.CharField(verbose_name="Автор", max_length=250)
    name = models.CharField(verbose_name="Название", max_length=250)
    md5 = models.CharField(verbose_name="MD5 сумма",max_length=100, null=True, blank=True)
    file = models.CharField(verbose_name="Путь к архиву", null=True, blank=True, max_length=500)
    created_date = models.DateTimeField(verbose_name="Дата создания", auto_now=True)

    class Meta:
        verbose_name = "Текущий архив"
        verbose_name_plural = "4. Текущие архивы"
        ordering = ['-created_date',]


    def __str__(self) -> str:
        return f"{self.project.name} - { self.name }"


from transliterate import slugify
def upload_file_to(instance, filename):
    related_model_id = instance.project_id

    project, assembly = str(instance.project.name), str(instance.assembly.name)
    project_translate, assembly_translate = slugify(project), slugify(assembly)

    project_path = project_translate if project_translate else project.replace(' ', '-').lower()
    assembly_path = assembly_translate if assembly_translate else assembly.replace(' ', '-').lower()

    print(f'Path: {project_path}/{assembly_path}/{filename}')

    directory_path = f"storage/models/{project_path}/{assembly_path}/"
    file_path = os.path.join(directory_path, filename)
    return file_path

class FileHistoryModel(models.Model):
    """ 
        История файлов ( содержит сам файл, потому что их может быть несколько )
    """
    project = models.ForeignKey(ProjectArchiveModel, verbose_name="Проект", related_name='project_history_files', on_delete=models.CASCADE)
    assembly = models.ForeignKey(AssemblyModel, verbose_name="Узел/Сборка", related_name='assembly_history_files', null=True, blank=True, on_delete=models.CASCADE)
    latest = models.ForeignKey(FileArchiveModel, verbose_name="Текущий архив", related_name='historical_files', on_delete=models.CASCADE)
    author = models.CharField(verbose_name="Автор", max_length=250)
    name = models.CharField(verbose_name="Название", max_length=250)
    md5 = models.CharField(verbose_name="MD5 сумма",max_length=100, null=True, blank=True)
    file = models.FileField(verbose_name="Архив файлов", upload_to=upload_file_to) 
    created_date = models.DateTimeField(verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Файл архива"
        verbose_name_plural = "5. Файлы архивов"
        ordering = ['-created_date',]

    def __str__(self) -> str:
        return self.name
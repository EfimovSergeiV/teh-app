from django.contrib import admin
from storage.models import (
    CategoryModel,
    AssemblyModel,
    ProjectArchiveModel, 
    FileArchiveModel,
    FileHistoryModel,
)

class CategoryAdmin(admin.ModelAdmin):
    """ Категории проектов """

    list_display = ('id', 'name',)
    list_display_links = ('id',)
    list_editable = ('name',)


class AssemblyAdmin(admin.ModelAdmin):
    """ Сборки/узлы проекта """
    list_display = ('id', 'name',)
    list_display_links = ('id',)
    list_filter = ('project',)



class FileArchiveAdmin(admin.TabularInline):
    """ Архивные файлы """

    model = FileArchiveModel
    readonly_fields = ('created_date', 'md5')
    # fk_name = 'project'

    fieldsets = (
        (None, {'fields': (('name', 'assembly', 'file', ),)}),
        (None, {'fields': (('author'),)}),
    )
    extra = 0



class ProjectArchiveAdmin(admin.ModelAdmin):
    """ """

    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name', 'created_date')
    readonly_fields = ('created_date', 'updated_date',)
    inlines = (FileArchiveAdmin,)


class FileHistoryAdmin(admin.ModelAdmin):
    """ """

    list_display = ('id', 'name', 'author', 'created_date')
    list_display_links = ('id', 'name')


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(AssemblyModel,AssemblyAdmin)
admin.site.register(ProjectArchiveModel, ProjectArchiveAdmin)
admin.site.register(FileHistoryModel, FileHistoryAdmin)
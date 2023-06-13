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
    search_fields = ('id', 'name',)
    list_editable = ('name',)
    list_filter = ('project',)



class FileArchiveAdmin(admin.TabularInline):
    """ Архивные файлы """

    model = FileArchiveModel
    readonly_fields = ('created_date', 'md5')
    # fk_name = 'project'
    list_filter = ('project',)

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
    search_fields = ('id', 'name',)
    list_filter = ('category',)
    inlines = (FileArchiveAdmin,)

from django.utils.safestring import mark_safe
from django.conf import settings
class FileArchiveAdmin(admin.ModelAdmin):
    def file_path(self, obj):
        return mark_safe('<a href="%sfiles/%s" target="blank">%sfiles/%s</a>' % (settings.BACKEND_URL,obj.file, settings.BACKEND_URL,str(obj.file)))
    file_path.short_description = 'Ссылка на архив'
    
    list_display = ('id', 'name', 'author', 'created_date')
    list_display_links = ('id', 'author', 'created_date')
    search_fields = ('id', 'name',)
    list_editable = ('name',)
    readonly_fields = ('file_path',)
    list_filter = ('project', 'assembly', 'author',)

class FileHistoryAdmin(admin.ModelAdmin):
    """ """

    list_display = ('id', 'name', 'author', 'created_date')
    list_display_links = ('id', 'author', 'created_date')
    search_fields = ('id', 'name',)
    list_editable = ('name',)
    list_filter = ('project', 'assembly', 'author',)


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(AssemblyModel,AssemblyAdmin)
admin.site.register(ProjectArchiveModel, ProjectArchiveAdmin)
admin.site.register(FileArchiveModel, FileArchiveAdmin)
admin.site.register(FileHistoryModel, FileHistoryAdmin)
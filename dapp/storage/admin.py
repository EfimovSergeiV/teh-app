from django.contrib import admin
from storage.models import (
    ProjectArchiveModel, 
    FileArchiveModel,
    FileHistoryModel,
)

class FileArchiveAdmin(admin.TabularInline):
    model = FileArchiveModel
    readonly_fields = ('created_date', 'md5')

    fieldsets = (
        (None, {'fields': (('name', 'md5', 'file', 'created_date'),)}),
        (None, {'fields': (('author'),)}),
    )
    extra = 0

class ProjectArchiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name', 'created_date')
    readonly_fields = ('created_date', )
    inlines = (FileArchiveAdmin,)


class FileHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_date')
    list_display_links = ('id', 'name')


admin.site.register(ProjectArchiveModel, ProjectArchiveAdmin)
admin.site.register(FileHistoryModel, FileHistoryAdmin)
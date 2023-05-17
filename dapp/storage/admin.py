from django.contrib import admin
from storage.models import ProjectArchiveModel, FileArchiveModel

class FileArchiveAdmin(admin.TabularInline):
    model = FileArchiveModel
    # readonly_fields = ('created_date', 'md5')

    fieldsets = (
        (None, {'fields': (('md5', 'file', 'created_date'),)}),
    )
    extra = 0

class ProjectArchiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name', 'created_date')
    readonly_fields = ('created_date', )
    inlines = (FileArchiveAdmin,)


admin.site.register(ProjectArchiveModel, ProjectArchiveAdmin)
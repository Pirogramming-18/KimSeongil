from django.contrib import admin
from .models import Tool, Idea
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class IdeaResource(resources.ModelResource):
    class Meta:
        model = Idea
        fields = ('id', 'title', 'image', 'content', 'interest', 'devtool')


class IdeaAdmin(ImportExportModelAdmin):
    fields = ('title', 'image', 'content', 'interest', 'devtool')
    list_display = ('id', 'title', 'image', 'content', 'interest', 'devtool')
    resource_class = IdeaResource


admin.site.register(Idea, IdeaAdmin)
admin.site.register(Tool)

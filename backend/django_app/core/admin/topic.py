from django.contrib import admin

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Topic
class TopicAdmin(admin.ModelAdmin):
    """
    Customizing admininterface for topic
    """
    
    fieldsets = (
        ('General Information', {'fields': ('title', 'description',)}),
    )

    list_display = ('title',)

# register SessionAdmin
admin.site.register(Topic, TopicAdmin)
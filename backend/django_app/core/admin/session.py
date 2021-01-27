from django.contrib import admin

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Session
class SessionAdmin(admin.ModelAdmin):
    """
    Customizing admininterface for ParlamentSession
    """
    
    fieldsets = (
        ('Parlament', {'fields': ('parlament',)}),
        ('General Information', {'fields': ('date', 'opening_session', 'regular_session', 'additional_information')}),
        ('Messages', {'fields': ('greeting', 'discharge',)}),
        ('Excused Councillors', {'fields': ('excused_politicans',)})
    )

    list_display = ('parlament', 'date', 'regular_session',)

# register SessionAdmin
admin.site.register(Session, SessionAdmin)
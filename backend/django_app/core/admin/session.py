from django.contrib import admin

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Session, Parlament

class SessionRessource(resources.ModelResource):
    parlament = fields.Field(column_name='parlament', attribute='parlament',
                                widget=ForeignKeyWidget(Parlament, 'pk'))
    opening_session = fields.Field(column_name='opening_session', attribute='opening_session',
                                widget=BooleanWidget())
    regular_session = fields.Field(column_name='regular_session', attribute='regular_session',
                                widget=BooleanWidget())

    class Meta:
        model = Parlament
        import_id_fields = ['id']

class SessionAdmin(ImportExportModelAdmin):
    """
    Customizing admininterface for ParlamentSession
    """
    
    fieldsets = (
        ('Parlament', {'fields': ('parlament',)}),
        ('General Information', {'fields': ('start_date', 'end_date', 'opening_session', 'regular_session', 'additional_information')}),
        ('Messages', {'fields': ('greeting', 'discharge',)}),
        ('Excused Councillors', {'fields': ('excused_politicans',)}),
        ('Files', {'fields': ('word_protocol',)}),
    )

    list_display = ('parlament', 'start_date', 'regular_session',)

# register SessionAdmin
admin.site.register(Session, SessionAdmin)
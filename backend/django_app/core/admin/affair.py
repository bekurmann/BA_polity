from django.contrib import admin

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Affair, Topic, Politican, Session, Parlament

class AffairRessource(resources.ModelResource):
    parlament = fields.Field(column_name='parlament', attribute='parlament', widget=ForeignKeyWidget(Parlament, 'pk'))
    signatory = fields.Field(column_name='signatory', attribute='signatory', widget=ManyToManyWidget(Politican, separator=';'))
    joint_signatories = fields.Field(column_name='joint_signatories', attribute='joint_signatories', widget=ManyToManyWidget(Politican, separator=';'))
    topics = fields.Field(column_name='topics', attribute='topics', widget=ManyToManyWidget(Topic, separator=';'))
    sessions = fields.Field(column_name='sessions', attribute='sessions', widget=ManyToManyWidget(Session, separator=';'))

    class Meta:
        model = Affair
        import_id_fields = ['id']

# *************************************************************************************
# Affair Admin
# *************************************************************************************

class AffairAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for Affair
    """
    readonly_fields = ['id',]
    raw_id_fields = ['signatory', 'joint_signatories',]

    fieldsets = (
        ('General Information', { 'fields': ('id', 'title', 'affair_type', 'status', 'urgent', 'identifier', 'date_received',) }),
        ('Belonging Parlament', {'fields': ('parlament', 'date_received',)}),
        ('Authorship', {'fields': ('signatory', 'joint_signatories_count', 'joint_signatories', 'commission',)}),
        ('Topics', {'fields': ('topics',)}),
        ('Content', {'fields': ('content_motivation', 'content_inquiries', 'content_all',)}),
        ('Sessions', {'fields': ('sessions',)}),   
    )

    resource_class = AffairRessource

    list_display = ('title', 'date_received', 'affair_type', 'status', 'identifier', 'parlament')
    search_fields = ['name' 'parlament',]

# register fraction
admin.site.register(Affair, AffairAdmin)

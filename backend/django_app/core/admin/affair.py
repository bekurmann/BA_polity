from django.contrib import admin

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Affair, AffairDebate, AffairFile, Topic, Politican, Session, Parlament

class AffairRessource(resources.ModelResource):
    parlament = fields.Field(column_name='parlament', attribute='parlament', widget=ForeignKeyWidget(Parlament, 'pk'))
    signatory = fields.Field(column_name='signatory', attribute='signatory', widget=ForeignKeyWidget(Politican, 'pk'))
    session = fields.Field(column_name='session', attribute='session', widget=ForeignKeyWidget(Session, 'pk'))
    joint_signatories = fields.Field(column_name='joint_signatories', attribute='joint_signatories', widget=ManyToManyWidget(Politican, separator=';'))
    topics = fields.Field(column_name='topics', attribute='topics', widget=ManyToManyWidget(Topic, separator=';'))

    class Meta:
        model = Affair
        import_id_fields = ['id']

class AffairDebateResource(resources.ModelResource):
    session = fields.Field(column_name='session', attribute='session',
                            widget=ForeignKeyWidget(Session, 'pk'))
    affair = fields.Field(column_name='affair', attribute='affair',
                            widget=ForeignKeyWidget(Affair, 'pk'))
    politican = fields.Field(column_name='politican', attribute='politican',
                            widget=ForeignKeyWidget(Politican, 'pk'))
    class Meta:
        model = AffairDebate
        import_id_fields = ['id']
class AffairFileResource(resources.ModelResource):
    affair = fields.Field(column_name='affair', attribute='affair',
                            widget=ForeignKeyWidget(Affair, 'pk'))
    class Meta:
        model = AffairFile
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
        ('General Information', { 'fields': ('id', 'title', 'affair_type', 'status', 'urgent', 'identifier', 'date_received', 'additional_information',) }),
        ('Belonging Parlament', {'fields': ('parlament',)}),
        ('Authorship', {'fields': ('signatory', 'joint_signatories_count', 'joint_signatories', 'commission',)}),
        ('Topics', {'fields': ('topics',)}),
        ('Content', {'fields': ('content_motivation', 'content_inquiries', 'content_all', 'content_response',)}),
        ('Session', {'fields': ('session',)}),
        ('Executive', {'fields': ('recommendation', 'transformation_recommendation',)}),  
        ('Anonymous Vote', {'fields': ('anon_yes', 'anon_no', 'anon_abstinence',)}),   
        ('Personalised Vote', {'fields': ('personalised_yes', 'personalised_no', 'personalised_abstinence',)}),  
        ('Result', {'fields': ('accepted',)}),  
        ('Special Fields', {'fields': ('discussion_desired', 'transformation_postulat',)}),  
    )

    resource_class = AffairRessource

    list_display = ('title', 'date_received', 'affair_type', 'status', 'identifier', 'parlament')
    search_fields = ['title', 'date_received', 'affair_type',]

# *************************************************************************************
# AffairDebate Admin
# *************************************************************************************

class AffairDebateAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for AffairDebate
    """
    readonly_fields = ['id']

    fieldsets = (
        ('General Information', {'fields': ('affair', 'politican', 'session', 'order',)}),
        ('Content', {'fields': ('content',)})
    )

    resource_class = AffairDebateResource

    list_display = ('politican', 'affair')
    search_fields = ['politican__first_name', 'politican__last_name', 'affair__title', 'content',]

# *************************************************************************************
# AffairFile Admin
# *************************************************************************************

class AffairFileAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for AffairFile
    """
    readonly_fields = ['id']

    fieldsets = (
        ('General Information', {'fields': ('id', 'affair', 'affair_file',)}),
    )

    resource_class = AffairFileResource

    list_display = ('affair', 'affair_file')

# register
admin.site.register(Affair, AffairAdmin)
admin.site.register(AffairDebate, AffairDebateAdmin)
admin.site.register(AffairFile, AffairFileAdmin)

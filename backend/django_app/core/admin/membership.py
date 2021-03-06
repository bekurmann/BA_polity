from django.contrib import admin

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Politican, Parlament, Commission, Membership

class MembershipRessource(resources.ModelResource):
    politican = fields.Field(column_name='politican', attribute='politican', widget=ForeignKeyWidget(Politican, 'pk'))
    parlament = fields.Field(column_name='parlament', attribute='parlament', widget=ForeignKeyWidget(Parlament, 'pk'))
    commission = fields.Field(column_name='commission', attribute='commission', widget=ForeignKeyWidget(Commission, 'pk'))
    #fraciton =

    class Meta:
        model = Membership
        import_id_fields = ['id']

# *************************************************************************************
# Membership Admin
# *************************************************************************************
class MembershipAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for Model Membership
    """
    raw_id_fields = ['politican']
    readonly_fields = ('active',)

    fieldsets = (
        ('Membership Type', {'fields': ('membership_type',)}),
        ('Membership Function', {'fields': ('membership_function',)}),
        ('Foreign Keys', {'fields': ('politican', 'parlament', 'commission','fraction',)}),
        ('Start- Enddate', {'fields': ('start_date', 'end_date',)}),
        ('Active (Calculated)', {'fields': ('active',)}),
    )

    resource_class = MembershipRessource

    list_display = ('politican', 
                    'membership_type', 'membership_function',  
                    'parlament', 'commission', 
                    'fraction', 'party',
                    'active',)


# register membership
admin.site.register(Membership, MembershipAdmin)
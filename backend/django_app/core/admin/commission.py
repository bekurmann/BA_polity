from django.contrib import admin

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Parlament, Commission
class CommissionRessource(resources.ModelResource):
    parlament = fields.Field(column_name='parlament', attribute='parlament', widget=ForeignKeyWidget(Parlament, 'pk'))

    class Meta:
        model = Commission
        import_id_fields = ['id']

# *************************************************************************************
# Commission Admin
# *************************************************************************************

class CommissionAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for Commission
    """
    fieldsets = (
        ('General Information', { 'fields': ('title', 'description', 'permanent', 'start_date', 'end_date',) }),
        ('Belonging Parlament', {'fields': ('parlament',)}),
        ('Contact', {'fields': ('email', 'website', 'phone')}),
    )

    resource_class = CommissionRessource

    list_display = ('title', 'parlament')
    search_fields = ['title' 'parlament',]

# register commission
admin.site.register(Commission, CommissionAdmin)
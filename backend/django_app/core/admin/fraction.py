from django.contrib import admin

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Parlament, Fraction

class FractionRessource(resources.ModelResource):
    parlament = fields.Field(column_name='parlament', attribute='parlament', widget=ForeignKeyWidget(Parlament, 'pk'))

    class Meta:
        model = Fraction
        import_id_fields = ['id']

# *************************************************************************************
# Fraction Admin
# *************************************************************************************

class FractionAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for Fraction
    """
    fieldsets = (
        ('General Information', { 'fields': ('name', 'abbreviation', 'description',) }),
        ('Belonging Parlament', {'fields': ('parlament',)}),
        ('Address & Contact', {'fields': ('street1', 'street2', 'city', 'email', 'website', 'phone')}),
    )

    resource_class = FractionRessource

    list_display = ('name', 'parlament')
    search_fields = ['name' 'parlament',]

# register fraction
admin.site.register(Fraction, FractionAdmin)

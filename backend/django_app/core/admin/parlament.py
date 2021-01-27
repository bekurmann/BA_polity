from django.contrib import admin

# avatar preview
from django.utils.safestring import mark_safe

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Parlament
from locations.models import Country, Canton, Municipality, PLZ

class ParlamentRessource(resources.ModelResource):
    city= fields.Field(column_name='city', attribute='city', widget=ForeignKeyWidget(PLZ, 'pk'))
    jurisdiction_country = fields.Field(column_name='jurisdiction_country', attribute='jurisdiction_country',
                            widget=ForeignKeyWidget(Country, 'pk'))
    jurisdiction_canton = fields.Field(column_name='jurisdiction_canton', attribute='jurisdiction_canton',
                            widget=ForeignKeyWidget(Canton, 'pk'))
    jurisdiction_municipality = fields.Field(column_name='jurisdiction_municipality', attribute='jurisdiction_municipality',
                            widget=ForeignKeyWidget(Municipality, 'pk'))

    class Meta:
        model = Parlament
        import_id_fields = ['id']

# *************************************************************************************
# Parlament Admin
# *************************************************************************************

class ParlamentAdmin(ImportExportModelAdmin):
    """
    Customizing Admininterface for Parlament
    """
    raw_id_fields = ['city']
    readonly_fields = ['get_avatar_preview']

    fieldsets = (
        ('General Information', { 'fields': ('title', 'description', 'number_of_seats',) }),
        ('Jurisdiction (Sparse)', {'fields': ('jurisdiction_country', 'jurisdiction_canton', 'jurisdiction_municipality',)}),
        ('Address', { 'fields': ('street1', 'street2', 'city')}),
        ('Location', { 'fields': ('location_query', 'location')}),
        ('Contact', {'fields': ('email', 'website', 'phone')}),
        ('Avatar', {'fields': ('avatar', 'get_avatar_preview')}),
    )

    resource_class = ParlamentRessource

    list_display = ('title', 'get_jurisdiction_name')
    search_fields = ['title' 'get_jurisdiction_name',]
    
    def get_jurisdiction_name(self, obj):
        # change depending on level
        if obj.jurisdiction_country != None:
            return obj.jurisdiction_country.name
        elif obj.jurisdiction_canton != None:
            return obj.jurisdiction_canton.name
        elif obj.jurisdiction_municipality != None:
            return obj.jurisdiction_municipality.name
        return "Unknown Jurisdiction"

    def get_avatar_preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" style="max-width: 150px" />')

# register parlament 
admin.site.register(Parlament, ParlamentAdmin)
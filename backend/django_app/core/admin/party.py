from django.contrib import admin

# avatar preview
from django.utils.safestring import mark_safe

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

# import models
from core.models import Party
from locations.models import PLZ

class PartyRessource(resources.ModelResource):
    city = fields.Field(column_name='jurisdiction', attribute='city',
                        widget=ForeignKeyWidget(PLZ, 'name'))

    class Meta:
        model = Party
        import_id_fields = ['id']

# *****************************************************************************************
# admin models
# *****************************************************************************************
class PartyAdmin(admin.ModelAdmin):
    """
    Customizing Admininterface for Model Council
    """
    raw_id_fields = ['city']
    readonly_fields = ['get_avatar_preview']

    fieldsets = (
        ('General Information', { 'fields': ('name', 'abbreviation', 'description', ) }),
        ('Parent', {'fields': ('parent',)}),
        ('Address', { 'fields': ('street1', 'street2', 'city',) }),
        ('Location', { 'fields': ('location_query', 'location',  ) }),
        ('Contact', { 'fields': ('email', 'website', 'phone' ) }),
        ('Avatar', { 'fields': ('avatar', 'get_avatar_preview', ) }),
    )

    resource_class = PartyRessource

    list_display = ('name', 'abbreviation',)
    search_fields = ['name' 'abbreviation', 'get_city_name',]

    # function for getting the city name (foreign key PLZ, field "name")
    def get_city_name(self, obj):
        return obj.city.name

    def get_avatar_preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" style="max-width: 150px" />')

admin.site.register(Party, PartyAdmin)
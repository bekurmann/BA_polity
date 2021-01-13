from django.contrib import admin
from django.contrib.gis import admin as GEOadmin

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from locations.models import Country, Region, Canton, Municipality, PLZ

# *****************************************************************************************
# import export ressources
# *****************************************************************************************

class PLZRessource(resources.ModelResource):
    bfs_nummer = fields.Field(column_name='bfs_nummer', attribute='bfs_nummer', 
                            widget=ForeignKeyWidget(Municipality, 'bfs_nummer'))
    class Meta:
        model = PLZ

# *****************************************************************************************
# admin models
# *****************************************************************************************

class CountryAdmin(GEOadmin.OSMGeoAdmin):
    """
    """
    list_display = ('name',)
    search_fields = ['name',]
class RegionAdmin(GEOadmin.OSMGeoAdmin):
    """
    """
    list_display = ('name',)
    search_fields = ['name',]
class CantonAdmin(GEOadmin.OSMGeoAdmin):
    """
    """
    readonly_fields = ['id']

    list_display = ('name',)
    search_fields = ['name',]

class MunicipalityAdmin(GEOadmin.OSMGeoAdmin):

    readonly_fields = ['id']
    
    list_display = ('name', 'bfs_nummer', 'kantonsnum',)
    search_fields = ['name', ]

class PLZAdmin(ImportExportModelAdmin):
    resource_class = PLZRessource

    readonly_fields = ['id']

    list_display = ('name', 'plz',)
    search_fields = ['name', 'plz',]


GEOadmin.site.register(Country, CountryAdmin)
GEOadmin.site.register(Region, RegionAdmin)
GEOadmin.site.register(Canton, CantonAdmin)
GEOadmin.site.register(Municipality, MunicipalityAdmin)

admin.site.register(PLZ, PLZAdmin)


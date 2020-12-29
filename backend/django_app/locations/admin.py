from django.contrib import admin
from django.contrib.gis import admin as GEOadmin


from locations.models import Country, Region, Canton, Municipality, PLZ

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
    list_display = ('name',)
    search_fields = ['name',]

class MunicipalityAdmin(GEOadmin.OSMGeoAdmin):
    list_display = ('name', 'bfs_nummer', 'kantonsnum',)
    search_fields = ['name', ]

class PLZAdmin(admin.ModelAdmin):
    list_display = ('name', 'plz',)
    search_fields = ['name', 'plz',]

GEOadmin.site.register(Country, CountryAdmin)
GEOadmin.site.register(Region, RegionAdmin)
GEOadmin.site.register(Canton, CantonAdmin)
GEOadmin.site.register(Municipality, MunicipalityAdmin)

admin.site.register(PLZ, PLZAdmin)
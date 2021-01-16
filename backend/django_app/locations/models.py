from django.db import models
from django.contrib.gis.db import models

"""
* PLZ from swisstopo:
    https://www.cadastre.ch/de/services/service/registry/plz.html

* Country, Canton, Region and Municipality import from swisstopo data:
    https://shop.swisstopo.admin.ch/de/products/landscape/boundaries3D

* careful regarding srid
    https://giswiki.hsr.ch/Koordinatensystem
* for lookup using srid=4326 (google; e.g. 46.993266740675786, 8.40434690011017 [latitude, longitude])
    from django.contrib.gis.geos import Point
    from locations.models import Canton
    pnt = Point(longitude, latitude) # e.g. Point(8.4043, 46.9932)
    pnt.transform(21781) # srid for switzerland lv03
    Canton.objects.filter(geom__contains=pnt)



    !!! still to do:
    * upload location, serializers, views
"""
class Country(models.Model):
    """
    """
    uuid = models.CharField(max_length=38)

    objektart = models.CharField(max_length=20)
    revision_q = models.CharField(max_length=100)
    icc = models.CharField(max_length=20)
    see_flaech = models.FloatField(null=True)
    name = models.CharField(max_length=254)
    landesflae = models.FloatField(null=True)
    land_teil = models.CharField(max_length=20)
    einwohnerz = models.BigIntegerField(null=True)

    # geodjango specific: a geometry field (multipolygonfield)
    # geom = models.MultiPolygonField(srid=21781)
    # automatically set srid for data (4326 is google/osm)
    geom = models.MultiPolygonField(srid=4326)

    # emblem
    def get_country_upload_path(instance, filename):
        return f'locations/country/{instance.name}_{instance.uuid}/{filename}'
    emblem = models.ImageField(upload_to=get_country_upload_path, blank=True, null=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # return string representation of the model
    def __str__(self):
        return f'{self.name}'
class Region(models.Model):
    """
    """
    uuid = models.CharField(max_length=38)

    # bezirksnum as identifier for foreignkey @canton und @municipality
    bezirksnum = models.BigIntegerField(unique=True, null=True)

    name = models.CharField(max_length=254)

    # foreign key canton
    kantonsnum = models.ForeignKey('Canton', to_field='kantonsnum', on_delete=models.CASCADE, blank=True, null=True)

    objektart = models.CharField(max_length=20)
    revision_q = models.CharField(max_length=100)
    icc = models.CharField(max_length=20)
    see_flaech = models.FloatField( null=True)
    bezirksfla = models.FloatField(null=True)
    bezirk_tei = models.CharField(max_length=20)
    einwohnerz = models.BigIntegerField(null=True)

    # geodjango specific: a geometry field (multipolygonfield)
    #geom = models.MultiPolygonField(srid=21781)
    geom = models.MultiPolygonField(srid=4326)

    # emblem
    def get_region_upload_path(instance, filename):
        return f'locations/region/{instance.name}_{instance.uuid}/{filename}'
    emblem = models.ImageField(upload_to=get_region_upload_path, blank=True, null=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # return string representation of the model
    def __str__(self):
        return f'{self.name}'

class Canton(models.Model):
    """
    """
    uuid = models.CharField(max_length=38)

    # kantonsnum as identifier for foreignkey @municipality
    kantonsnum = models.BigIntegerField(unique=True)

    name = models.CharField(max_length=254)
    abbreviation = models.CharField(blank=True, max_length=20)
    objektart = models.CharField(max_length=20)
    revision_q = models.CharField(max_length=100)
    icc = models.CharField(max_length=20)
    see_flaech = models.FloatField(null=True)
    kantonsfla = models.FloatField(null=True)
    kt_teil = models.CharField(max_length=20)
    einwohnerz = models.BigIntegerField(null=True)

    # geodjango specific: a geometry field (multipolygonfield)
    #geom = models.MultiPolygonField(srid=21781)
    geom = models.MultiPolygonField(srid=4326)

    # emblem
    def get_canton_upload_path(instance, filename):
        return f'locations/canton/{instance.name}_{instance.uuid}/{filename}'
    emblem = models.ImageField(upload_to=get_canton_upload_path, blank=True, null=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # return string representation of the model
    def __str__(self):
        return f'{self.name}'
  

class Municipality(models.Model):
    uuid = models.CharField(max_length=38)

    # foreign key canton
    kantonsnum = models.ForeignKey(Canton, to_field='kantonsnum', related_name='cantons', on_delete=models.CASCADE, blank=True, null=True)

    # foreign key bezirk
    bezirksnum = models.ForeignKey(Region, to_field='bezirksnum', related_name='regions', on_delete=models.CASCADE, blank=True, null=True)

    # bfs_nummer as identifier for foreign key locations.PLZ (needs unique=True)
    bfs_nummer = models.BigIntegerField(unique=True, null=True)

    name = models.CharField(max_length=254)
    objektart = models.CharField(max_length=20)
    revision_q = models.CharField(max_length=100)
    icc = models.CharField(max_length=20)
    see_flaech = models.FloatField(null=True)
    gem_flaech = models.FloatField(null=True)
    gem_teil = models.CharField(max_length=20)
    shn = models.CharField(max_length=20, null=True)
    einwohnerz = models.BigIntegerField(null=True)

    # geodjango specific: a geometry field (multipolygonfield)
    #geom = models.MultiPolygonField(srid=21781)
    geom = models.MultiPolygonField(srid=4326)

    # emblem
    def get_municipality_upload_path(instance, filename):
        return f'locations/municipality/{instance.name}_{instance.uuid}/{filename}'
    emblem = models.ImageField(upload_to=get_municipality_upload_path, blank=True, null=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # return string representation of the model
    def __str__(self):
        return f'{self.name}'

class PLZ(models.Model):
    # foreign key municipality using bfs_nummer
    bfs_nummer = models.ForeignKey(Municipality, to_field='bfs_nummer', related_name='municipalities', on_delete=models.CASCADE, blank=True, null=True)

    plz = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # return string representation of the model
    def __str__(self):
        return f'{self.name} {self.plz}'
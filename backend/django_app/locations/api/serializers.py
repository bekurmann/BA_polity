from rest_framework import serializers

from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from rest_framework_gis.fields import GeometryField

from locations.models import Country, Region, Canton, Municipality, PLZ

class CountrySerializer(GeoFeatureModelSerializer):
    """
    serialize country as geojson compatible data
    """
    geom = GeometryField() # precision=1, remove_duplicates=True

    class Meta:
        model = Country
        geo_field = 'geom'

        fields = '__all__'

class RegionSerializer(GeoFeatureModelSerializer):
    """
    serialize country as geojson compatible data
    """

    geom = GeometryField()

    class Meta:
        model = Region
        geo_field = 'geom'

        fields = '__all__'
class CantonSerializer(GeoFeatureModelSerializer):
    """
    serialize country as geojson compatible data
    """
    geom = GeometryField()

    class Meta:
        model = Canton
        geo_field = 'geom'

        fields = '__all__'
        #fields = ('kantonsnum', 'name', 'see_flaech', 'kantonsfla', 'einwohnerz', 'emblem', '')

class CantonNestedSerializer(serializers.ModelSerializer):
    """
    serialize canton without geom and geojson (for nesting in parlament)
    """
    class Meta:
        model = Canton
        exclude = ['geom']

class MunicipalitySerializer(GeoFeatureModelSerializer):
    """
    serialize country as geojson compatible data
    """
    geom = GeometryField()
    class Meta:
        model = Municipality
        geo_field = 'geom'

        fields = '__all__'

class PLZSerializer(serializers.ModelSerializer):
    """
    serialize plz
    """
    class Meta:
        model = PLZ
        exclude = ['id', 'created_at', 'updated_at']
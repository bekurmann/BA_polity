from rest_framework import serializers

from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField

from locations.models import Country, Region, Canton, Municipality, PLZ

# topojson
import topojson

class CountrySerializer(GeoFeatureModelSerializer):
    """
    serialize country as geojson compatible data
    """
    topojson_geom = GeometrySerializerMethodField()

    def get_topojson_geom(self, obj):
        # Returns a new GEOSGeometry, simplified to the specified tolerance
        # using the Douglas-Peucker algorithm. A higher tolerance value implies
        # fewer points in the output. If no tolerance is provided, it
        # defaults to 0.
        return obj.geom.simplify(tolerance=0.05, preserve_topology=True)

    class Meta:
        model = Country
        geo_field = 'simplified_geom'

        fields = '__all__'

class RegionSerializer(GeoFeatureModelSerializer):
    """
    serialize country as geojson compatible data
    """
    simplified_geom = GeometrySerializerMethodField()

    def get_simplified_geom(self, obj):
        # Returns a new GEOSGeometry, simplified to the specified tolerance
        # using the Douglas-Peucker algorithm. A higher tolerance value implies
        # fewer points in the output. If no tolerance is provided, it
        # defaults to 0.
        return obj.geom.simplify(tolerance=0.05, preserve_topology=True)

    class Meta:
        model = Region
        geo_field = 'simplified_geom'

        fields = '__all__'
class CantonSerializer(GeoFeatureModelSerializer):
    """
    serialize country as geojson compatible data
    """
    simplified_geom = GeometrySerializerMethodField()

    def get_simplified_geom(self, obj):
        # Returns a new GEOSGeometry, simplified to the specified tolerance
        # using the Douglas-Peucker algorithm. A higher tolerance value implies
        # fewer points in the output. If no tolerance is provided, it
        # defaults to 0.
        return obj.geom.simplify(tolerance=0.05, preserve_topology=True)

    class Meta:
        model = Canton
        geo_field = 'simplified_geom'

        fields = '__all__'
        #fields = ('kantonsnum', 'name', 'see_flaech', 'kantonsfla', 'einwohnerz', 'emblem', '')

class MunicipalitySerializer(GeoFeatureModelSerializer):
    """
    serialize country as geojson compatible data
    """
    simplified_geom = GeometrySerializerMethodField()

    def get_simplified_geom(self, obj):
        # Returns a new GEOSGeometry, simplified to the specified tolerance
        # using the Douglas-Peucker algorithm. A higher tolerance value implies
        # fewer points in the output. If no tolerance is provided, it
        # defaults to 0.
        return obj.geom.simplify(tolerance=0.05, preserve_topology=True)

    class Meta:
        model = Municipality
        geo_field = 'simplified_geom'

        fields = '__all__'
class PLZSerializer(serializers.ModelSerializer):

    class Meta:
        model = PLZ
        exclude = ['id', 'created_at', 'updated_at']
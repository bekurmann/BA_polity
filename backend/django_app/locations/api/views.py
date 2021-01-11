from rest_framework import viewsets

from locations.models import Country, Canton, Region, Municipality

from locations.api.serializers import CountrySerializer, CantonSerializer, RegionSerializer, MunicipalitySerializer

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-onyl viewset for country model
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CantonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-onyl viewset for country model
    """
    queryset = Canton.objects.all()
    serializer_class = CantonSerializer

class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-onyl viewset for country model
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class MunicipalityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-onyl viewset for country model
    """
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
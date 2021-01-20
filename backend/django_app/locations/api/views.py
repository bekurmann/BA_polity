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

class NestedMunicipalityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for municipalities in canton x
    """
    def get_queryset(self):
        return Municipality.objects.filter(kantonsnum=self.kwargs['kantonsnum_pk'])

    serializer_class = MunicipalitySerializer
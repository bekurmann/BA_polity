from rest_framework import viewsets

from politicans.models import Politican
from politicans.api.serializers import PoliticanSerializer

class PoliticanViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing politicans & detailview based on pk
    """
    queryset = Politican.objects.all()
    serializer_class = PoliticanSerializer

class PoliticanParlamentMembershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlament membership for politican
    """
    pass
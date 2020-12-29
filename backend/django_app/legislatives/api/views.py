from rest_framework import viewsets

from legislatives.models import Parlament, Commission
from legislatives.api.serializers import ParlamentSerializer, CommissionSerializer

class ParlamentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlaments & detailview based on pk
    """
    queryset = Parlament.objects.all()
    serializer_class = ParlamentSerializer

class CommissionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing commissions & detailview based on pk
    """
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer
from rest_framework import viewsets

# models
from core.models import Parlament

# serializers
from core.api.serializers import ParlamentSerializer

# *****************************************************************************************
# Parlament
# *****************************************************************************************
class ParlamentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlaments
    """
    queryset = Parlament.objects.all()
    serializer_class = ParlamentSerializer
from rest_framework import viewsets

# models
from core.models import Fraction

# serializers
from core.api.serializers import FractionSerializer

# *****************************************************************************************
# Fraction
# *****************************************************************************************
class FractionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing fractions
    """
    def get_queryset(self):
        return Fraction.objects.filter(parlament=self.kwargs['parlament_pk']).order_by('id')

    serializer_class = FractionSerializer
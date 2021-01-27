from rest_framework import viewsets

# models
from core.models import Commission

# serializers
from core.api.serializers import CommissionSerializer

# *****************************************************************************************
# Commission
# *****************************************************************************************
class CommissionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing commissions
    """
    def get_queryset(self):
        return Commission.objects.filter(parlament=self.kwargs['parlament_pk'])

    serializer_class = CommissionSerializer
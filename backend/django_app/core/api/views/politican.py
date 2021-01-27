from rest_framework import viewsets

# models
from core.models import Politican, Membership

# serializers
from core.api.serializers import PoliticanSerializer, MembershipSerializer

class PoliticanViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing politicans & detailview based on pk
    """
    queryset = Politican.objects.all()
    serializer_class = PoliticanSerializer

class PoliticanParlamentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlament membership for politican
    """
    def get_queryset(self):
        return Membership.objects.filter(politican=self.kwargs['politican_pk'])

    serializer_class = MembershipSerializer
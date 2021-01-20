from rest_framework import viewsets

from politicans.models import Politican
from politicans.api.serializers import PoliticanSerializer

from legislatives.models import Membership
from legislatives.api.serializers import MembershipSerializer

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
    

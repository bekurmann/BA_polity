from rest_framework import viewsets

# models
from core.models import Politican, Membership

# serializers
from core.api.serializers import PoliticanListSerializer, PoliticanDetailSerializer, MembershipSerializer

class PoliticanViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing politicans & detailview based on pk
    """
    queryset = Politican.objects.all()
    serializer_class = PoliticanListSerializer
    detail_serializer_class = PoliticanDetailSerializer

    def get_serializer_class(self):
        # return serializer class based on action (list/retrieve)
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        
        return super(PoliticanViewSet, self).get_serializer_class()

class PoliticanParlamentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlament membership for politican
    """
    def get_queryset(self):
        return Membership.objects.filter(politican=self.kwargs['politican_pk'])

    serializer_class = MembershipSerializer
    
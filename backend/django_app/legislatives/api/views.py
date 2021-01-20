from rest_framework import viewsets

from legislatives.models import ( Parlament, ParlamentSession, 
                                Membership,
                                Commission )
from legislatives.api.serializers import ( ParlamentSerializer, ParlamentSessionSerializer,
                                        MembershipSerializer, 
                                        CommissionSerializer )
                                        
# *****************************************************************************************
# Parlament
# *****************************************************************************************

class ParlamentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlaments
    """
    queryset = Parlament.objects.all()
    serializer_class = ParlamentSerializer

class ParlamentSessionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing sessions of specific parlament
    """
    def get_queryset(self):
        return ParlamentSession.objects.filter(parlament=self.kwargs['parlament_pk'])

    serializer_class = ParlamentSessionSerializer
    
    
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

# *****************************************************************************************
# Memberships
# *****************************************************************************************
class ParlamentMembershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlament membership
    """
    def get_queryset(self):
        return Membership.objects.filter(parlament=self.kwargs['parlament_pk'])

    serializer_class = MembershipSerializer 

class CommissionMembershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing commission membership
    """
    def get_queryset(self):
        return Membership.objects.filter(commission=self.kwargs['commission_pk'])

    serializer_class = MembershipSerializer 
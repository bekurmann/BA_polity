from rest_framework import viewsets

from legislatives.models import ( Parlament, ParlamentMembership, ParlamentMembershipRole,
                                Commission, CommissionMembership, CommissionMembershipRole )
from legislatives.api.serializers import ( ParlamentSerializer, CommissionSerializer, 
                                            CommissionMembershipSerializer, CommissionMembershipRoleSerializer )
                                        
# *****************************************************************************************
# Parlament
# *****************************************************************************************

class ParlamentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlaments
    """
    queryset = Parlament.objects.all()
    serializer_class = ParlamentSerializer

class ParlamentMembershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlament members
    """
    def get_queryset(self):
        return ParlamentMembership.objects.filter(parlament=self.kwargs['parlament_pk'])
    

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

class CommissionMembershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing commission members
    """
    def get_queryset(self):
        return CommissionMembership.objects.filter(commission=self.kwargs['commission_pk'])

    serializer_class = CommissionMembershipSerializer

class CommissionMembershipRoleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing roles of commission members
    """
    def get_queryset(self):
        return CommissionMembershipRole.objects.filter(commission_membership=self.kwargs['commission_membership_pk'])

    serializer_class = CommissionMembershipRoleSerializer
    
    


from rest_framework import viewsets

from legislatives.models import ( Parlament, ParlamentSession, 
                                ParlamentMembership, ParlamentMembershipRole,
                                Commission, CommissionMembership, CommissionMembershipRole )
from legislatives.api.serializers import ( ParlamentSerializer, ParlamentSessionSerializer,
                                        ParlamentMembershipSerializer, 
                                        ParlamentMembershipRoleSerializer,
                                        CommissionSerializer, CommissionMembershipSerializer, 
                                        CommissionMembershipRoleSerializer )
                                        
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
    read-only viewset for listing parlament sessions
    """
    def get_queryset(self):
        return ParlamentSession.objects.filter(parlament=self.kwargs['parlament_pk'])

    serializer_class = ParlamentSessionSerializer
    

class ParlamentMembershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlament members
    """
    def get_queryset(self):
        return ParlamentMembership.objects.filter(parlament=self.kwargs['parlament_pk'])

    serializer_class = ParlamentMembershipSerializer

class ParlamentMembershipRoleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing roles of parlament members
    """
    def get_queryset(self):
        return ParlamentMembershipRole.objects.filter(parlament_membership=self.kwargs['parlament_membership_pk'])

    serializer_class = ParlamentMembershipRoleSerializer
    
    

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
    
    


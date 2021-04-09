from rest_framework import viewsets

# models
from core.models import Membership

# serializers
from core.api.serializers import MembershipListSerializer, MembershipDetailSerializer

# *****************************************************************************************
# Memberships
# *****************************************************************************************
class ParlamentMembershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlament membership
    """
    def get_queryset(self):
        # returns all memberships with function member of politicans in parlament (only active ones)
        return Membership.objects.filter(parlament=self.kwargs['parlament_pk'],
                                        membership_type="PARLA" or "FRACT",
                                        membership_function="MEMBE",
                                        # all with empty end_date (meaning still active)
                                        #end_date__isnull=True,
                                        )

    serializer_class = MembershipListSerializer 
    detail_serializer_class = MembershipDetailSerializer

    def get_serializer_class(self):
        # return serializer class based on action (list/retrieve)
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        
        return super(ParlamentMembershipViewSet, self).get_serializer_class()

class CommissionMembershipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing commission membership
    """
    def get_queryset(self):
        return Membership.objects.filter(commission=self.kwargs['commission_pk'])

    serializer_class = MembershipListSerializer 
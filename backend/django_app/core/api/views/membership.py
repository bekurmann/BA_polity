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
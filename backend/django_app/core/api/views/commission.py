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
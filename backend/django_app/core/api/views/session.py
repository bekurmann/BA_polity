class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing sessions
    """
    def get_queryset(self):
        return Session.objects.filter(parlament=self.kwargs['parlament_pk'])

    serializer_class = SessionSerializer
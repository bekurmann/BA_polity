from rest_framework import viewsets

# models
from core.models import Session

# serializers
from core.api.serializers import SessionSerializer

class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing sessions
    """
    def get_queryset(self):
        return Session.objects.filter(parlament=self.kwargs['parlament_pk'])

    serializer_class = SessionSerializer
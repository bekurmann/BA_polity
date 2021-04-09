from rest_framework import viewsets

# models
from core.models import Parlament

# serializers
from core.api.serializers import ParlamentListSerializer, ParlamentDetailSerializer

# *****************************************************************************************
# Parlament
# *****************************************************************************************
class ParlamentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for listing parlaments
    """
    queryset = Parlament.objects.all()
    serializer_class = ParlamentListSerializer
    detail_serializer_class = ParlamentDetailSerializer

    def get_serializer_class(self):
        # return serializer class based on action (list/retrieve)
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        
        return super(ParlamentViewSet, self).get_serializer_class()

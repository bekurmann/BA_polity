from rest_framework import viewsets

# models
from core.models import Affair, AffairDebate, AffairFile

# serializers
from core.api.serializers import ( AffairListSerializer, AffairDetailSerializer,
                                    AffairDebateListSerializer, AffairDebateDetailSerializer,
                                    AffairFileListSerializer, AffairFileDetailSerializer )

# *****************************************************************************************
# Affair
# *****************************************************************************************
class AffairViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for affairs
    """
    def get_queryset(self):
        return Affair.objects.filter(parlament=self.kwargs['parlament_pk'])

    serializer_class = AffairListSerializer
    detail_serializer_class = AffairDetailSerializer

    def get_serializer_class(self):
        # return serializer class based on action (list/retrieve)
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        
        return super(AffairViewSet, self).get_serializer_class()
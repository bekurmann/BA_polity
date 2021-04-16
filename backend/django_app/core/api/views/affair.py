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
class AffairAllViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for all affairs (not nested)
    """
    def get_queryset(self):
        return Affair.objects.all()

    serializer_class = AffairListSerializer
    detail_serializer_class = AffairDetailSerializer

    def get_serializer_class(self):
        # return serializer class based on action (list/retrieve)
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        
        return super(AffairAllViewSet, self).get_serializer_class()
class AffairViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for affairs based on parlament (nested route)
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


# *****************************************************************************************
# AffairDebate
# *****************************************************************************************
class AffairDebateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for affairs
    """
    def get_queryset(self):
        return AffairDebate.objects.filter(affair=self.kwargs['affair_pk']).order_by('order')

    serializer_class = AffairDebateListSerializer
    detail_serializer_class = AffairDebateDetailSerializer

    def get_serializer_class(self):
        # return serializer class based on action (list/retrieve)
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        
        return super(AffairDebateViewSet, self).get_serializer_class()

# *****************************************************************************************
# AffairFile
# *****************************************************************************************
class AffairFileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read-only viewset for affairs
    """
    def get_queryset(self):
        return AffairFile.objects.filter(affair=self.kwargs['affair_pk'])

    serializer_class = AffairFileListSerializer
    detail_serializer_class = AffairFileDetailSerializer

    def get_serializer_class(self):
        # return serializer class based on action (list/retrieve)
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        
        return super(AffairFileViewSet, self).get_serializer_class()
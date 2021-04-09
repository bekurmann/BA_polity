from rest_framework import serializers

# import models
from core.models import Parlament

# import additional serializers 
from locations.api.serializers import CantonNestedSerializer, PLZSerializer

# *****************************************************************************************
# Parlament
# *****************************************************************************************
class ParlamentListSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Parlament
        exclude = ['location', 'location_query',]

class ParlamentDetailSerializer(serializers.ModelSerializer):
    """ 
    model serializer for parlament
        * city is nested with PLZSerializer
        * notice excluded fields
    """
    city = PLZSerializer(read_only=True)
    jurisdiction_canton = CantonNestedSerializer(read_only=True)

    class Meta:
        model = Parlament
        exclude = ['created_at', 'updated_at', 'location_query']
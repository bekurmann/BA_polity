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

    number_of_registered_members = serializers.SerializerMethodField()
    number_of_fractions = serializers.SerializerMethodField()

    class Meta:
        model = Parlament
        exclude = ['created_at', 'updated_at', 'location_query']

    def get_number_of_registered_members(self, members):
        return members.parlament_memberships.filter(
                        membership_type="PARLA", 
                        membership_function="MEMBE"
                        ).count()

    def get_number_of_fractions(self, fractions):
        return fractions.fractions.count()

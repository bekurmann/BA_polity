from rest_framework import serializers

from legislatives.models import ( Parlament, ParlamentSession, ParlamentMembership, 
                                Commission, CommissionMembership ) 
from locations.api.serializers import PLZSerializer
from politicans.api.serializers import PoliticanSerializer

# *****************************************************************************************
# Parlament
# *****************************************************************************************
class ParlamentSerializer(serializers.ModelSerializer):
    """ 
    model serializer for parlament
        * city is nested with PLZSerializer
        * notice excluded fields
    """
    city = PLZSerializer(read_only=True)

    class Meta:
        model = Parlament
        exclude = ['created_at', 'updated_at', 'location_query']

class ParlamentSessionSerializer(serializers.ModelSerializer):
    """
    model serializer for parlamentsession
    """
    class Meta:
        model = ParlamentSession
        exclude = ['created_at', 'updated_at', ]
class ParlamentMembershipSerializer(serializers.ModelSerializer):
    """
    model serializer for parlament memberships
    """
    politican = PoliticanSerializer(read_only=True)
    active = serializers.BooleanField()
    class Meta:
        model = ParlamentMembership
        exclude = [ 'created_at', 'updated_at',]

# *****************************************************************************************
# Commission
# *****************************************************************************************

class CommissionSerializer(serializers.ModelSerializer):
    """
    model serializer for commission
    """
    class Meta:
        model = Commission
        exclude = ['created_at', 'updated_at',]

class CommissionMembershipSerializer(serializers.ModelSerializer):
    """
    model serializer for CommissionMembership
    """
    politican = PoliticanSerializer(read_only=True)
    class Meta:
        model = CommissionMembership
        exclude = ['created_at', 'updated_at',]

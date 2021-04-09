from rest_framework import serializers

# import models
from core.models import Membership

from core.api.serializers import PoliticanListSerializer

# *****************************************************************************************
# Membership
# *****************************************************************************************
class MembershipListSerializer(serializers.ModelSerializer):
    """
    model serializer for membership
    """
    politican = PoliticanListSerializer(read_only=True)
    active = serializers.BooleanField()
    class Meta:
        model = Membership
        exclude = [ 'created_at', 'updated_at',]

class MembershipDetailSerializer(serializers.ModelSerializer):
    """
    model serializer for membership
    """
    politican = PoliticanListSerializer(read_only=True)
    active = serializers.BooleanField()
    class Meta:
        model = Membership
        exclude = [ 'created_at', 'updated_at',]        
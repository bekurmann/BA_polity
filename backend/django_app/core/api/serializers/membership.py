from rest_framework import serializers

# import models
from core.models import Membership

from core.api.serializers import PoliticanSerializer

# *****************************************************************************************
# Membership
# *****************************************************************************************
class MembershipSerializer(serializers.ModelSerializer):
    """
    model serializer for membership
    """
    politican = PoliticanSerializer(read_only=True)
    active = serializers.BooleanField()
    class Meta:
        model = Membership
        exclude = [ 'created_at', 'updated_at',]
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


    # I needed to "flatten" json response because of v-data-iterator (only one level possible)    
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    class Meta:
        model = Membership
        exclude = [ 'created_at', 'updated_at',]

    def get_first_name(self, membership):
        return membership.politican.first_name

    def get_last_name(self, membership):
        return membership.politican.last_name

    def get_city(self, membership):
        return membership.politican.city.name

class MembershipDetailSerializer(serializers.ModelSerializer):
    """
    model serializer for membership
    """
    politican = PoliticanListSerializer(read_only=True)
    active = serializers.BooleanField()
    class Meta:
        model = Membership
        exclude = [ 'created_at', 'updated_at',]        
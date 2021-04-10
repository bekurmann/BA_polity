from rest_framework import serializers

# import models
from core.models import Parlament, Affair, AffairDebate

# import additional serializers 
from locations.api.serializers import CantonNestedSerializer, PLZSerializer

# import for prefetching
from django.db.models import Prefetch

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
    number_of_affairs = serializers.SerializerMethodField()
    number_of_debate_statements = serializers.SerializerMethodField()
    number_of_sessions = serializers.SerializerMethodField()

    class Meta:
        model = Parlament
        exclude = ['created_at', 'updated_at', 'location_query']

    def get_number_of_registered_members(self, parlament):
        return parlament.parlament_memberships.filter(
                        membership_type="PARLA", 
                        membership_function="MEMBE"
                        ).count()

    def get_number_of_fractions(self, parlament):
        return parlament.fractions.count()

    def get_number_of_affairs(self, parlament):
        return parlament.affairs_parlaments.count()

    def get_number_of_debate_statements(self, parlament):
        debates = AffairDebate.objects.filter(affair__parlament=parlament)
        return debates.count()

    def get_number_of_sessions(self, parlament):
        return parlament.parlaments.count()

    

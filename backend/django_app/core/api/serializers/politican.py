from rest_framework import serializers

# import models
from core.models import Politican, Affair, AffairDebate

# import additional serializers 
from locations.api.serializers import PLZSerializer
from core.api.serializers import (FractionSerializer, CommissionSerializer, 
                                    AffairDetailSerializer, AffairDebateListSerializer)

class PoliticanListSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
    fractions = FractionSerializer(read_only=True, many=True)

    class Meta:
        model = Politican
        exclude = ['profession', 'date_of_birth', 'parlaments',
                    'email', 'website',
                    'location_query', 
                    'parties', 'executives', 'commissions', 'title', 'street1', 
                    'street2', 'phone',]

class PoliticanDetailSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
    fractions = FractionSerializer(read_only=True, many=True)
    commissions = CommissionSerializer(read_only=True, many=True)
    #parties = 
    #parlaments = ParlamentSerializer(read_only=True)

    affairs = serializers.SerializerMethodField()
    debate_statements = serializers.SerializerMethodField()

    number_of_submitted_affairs = serializers.SerializerMethodField()
    number_of_successful_affairs = serializers.SerializerMethodField()
    number_of_debate_statements = serializers.SerializerMethodField()
    number_of_successful_affairs = serializers.SerializerMethodField()
 
    class Meta:
        model = Politican
        exclude = ['location_query', ]

    def get_number_of_submitted_affairs(self, politican):
        # wrong related name, should be affairs
        return politican.signatories.count()

    def get_number_of_successful_affairs(self, politican):
        success = Affair.objects.filter(signatory=politican, accepted=True).count()
        return success

    def get_affairs(self, politican):
        # returns all affairs (nested) where politican is signatory
        affairs = Affair.objects.filter(signatory=politican)
        affairs_serializer = AffairDetailSerializer(affairs, many=True)
        return affairs_serializer.data
    
    def get_number_of_debate_statements(self, politican):
        return politican.affairdebates.count()

    def get_debate_statements(self, politican):
        statements = AffairDebate.objects.filter(politican=politican)
        statements_serializer = AffairDebateListSerializer(statements, many=True)
        return statements_serializer.data

    
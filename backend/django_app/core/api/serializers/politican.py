from rest_framework import serializers

# import models
from core.models import Politican

# import additional serializers 
from locations.api.serializers import PLZSerializer
from core.api.serializers import FractionSerializer, CommissionSerializer

class PoliticanListSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
    fractions = FractionSerializer(read_only=True, many=True)

    class Meta:
        model = Politican
        exclude = ['profession', 'date_of_birth', 'parlaments',
                    'email', 'website',
                    'location_query', 
                    'parties', 'executives', 'commissions', 'title', 'street1', 
                    'street2', 'location', 'phone',]

class PoliticanDetailSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
    fractions = FractionSerializer(read_only=True, many=True)
    commissions = CommissionSerializer(read_only=True, many=True)
    #parties = 
    #parlaments = ParlamentSerializer(read_only=True)

    number_of_submitted_affairs = serializers.SerializerMethodField()
    number_of_debate_statements = serializers.SerializerMethodField()
 
    class Meta:
        model = Politican
        exclude = ['location_query', ]

    def get_number_of_submitted_affairs(self, politican):
        # wrong related name, should be affairs
        return politican.signatories.count()

    def get_number_of_debate_statements(self, politican):
        return politican.affairdebates.count()
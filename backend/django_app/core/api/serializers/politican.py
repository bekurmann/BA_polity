from rest_framework import serializers

# import models
from core.models import Politican

# import additional serializers 
from locations.api.serializers import PLZSerializer
from core.api.serializers import FractionSerializer, CommissionSerializer

class PoliticanListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Politican
        exclude = ['profession', 'date_of_birth', 'parlaments', 'fractions', 
                    'email', 'website',
                    'location_query', 'location', 
                    'parties', 'executives', 'commissions',]

class PoliticanDetailSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
    fractions = FractionSerializer(read_only=True, many=True)
    commissions = CommissionSerializer(read_only=True, many=True)
    #parties = 
    #parlaments = ParlamentSerializer(read_only=True)
 
    class Meta:
        model = Politican
        exclude = ['location_query', ]
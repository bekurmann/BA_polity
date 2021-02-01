from rest_framework import serializers

# import models
from core.models import Politican

# import additional serializers 
from locations.api.serializers import PLZSerializer
from core.api.serializers import FractionSerializer, CommissionSerializer


class PoliticanSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
    fractions = FractionSerializer(read_only=True, many=True)
    commissions = CommissionSerializer(read_only=True, many=True)
    #parties = 
    #parlaments = ParlamentSerializer(read_only=True)
 
    class Meta:
        model = Politican
        exclude = ['location_query', ]
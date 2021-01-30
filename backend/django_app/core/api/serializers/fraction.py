from rest_framework import serializers

# import models
from core.models import Fraction

#from core.api.serializers import ParlamentSerializer

class FractionSerializer(serializers.ModelSerializer):
    """
    model serializer for fraction
    """
    #parlament = ParlamentSerializer(read_only=True, many=True)

    class Meta:
        model = Fraction
        exclude = ['created_at', 'parlament',]
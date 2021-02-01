from rest_framework import serializers

# import models
from core.models import Fraction

class FractionSerializer(serializers.ModelSerializer):
    """
    model serializer for fraction
    """

    class Meta:
        model = Fraction
        fields = '__all__'
from rest_framework import serializers

# import models
from core.models import Commission

# *****************************************************************************************
# Commission
# *****************************************************************************************
class CommissionSerializer(serializers.ModelSerializer):
    """
    model serializer for commission
    """
    class Meta:
        model = Commission
        exclude = ['created_at', 'updated_at',]
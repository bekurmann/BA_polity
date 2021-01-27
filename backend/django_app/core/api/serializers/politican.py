from rest_framework import serializers

# import models
from core.models import Politican

# import additional serializers 
from locations.api.serializers import PLZSerializer

class PoliticanSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
 
    class Meta:
        model = Politican
        exclude = ['created_at', 'updated_at', 'location_query', ]
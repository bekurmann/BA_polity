from rest_framework import serializers

from politicans.models import Politican

# import for field city -> bfs_nummer -> municipality GIS
from locations.api.serializers import PLZSerializer

class PoliticanSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
 
    class Meta:
        model = Politican
        exclude = ['created_at', 'updated_at', 'location_query', ]

from rest_framework import serializers

from locations.models import PLZ

class PLZSerializer(serializers.ModelSerializer):

    class Meta:
        model = PLZ
        exclude = ['id', 'created_at', 'updated_at']
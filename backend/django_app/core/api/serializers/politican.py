class PoliticanSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
 
    class Meta:
        model = Politican
        exclude = ['created_at', 'updated_at', 'location_query', ]
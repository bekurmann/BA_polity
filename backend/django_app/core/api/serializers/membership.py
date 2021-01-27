# *****************************************************************************************
# Membership
# *****************************************************************************************
class MembershipSerializer(serializers.ModelSerializer):
    """
    model serializer for membership
    """
    politican = PoliticanSerializer(read_only=True)
    active = serializers.BooleanField()
    class Meta:
        model = Membership
        exclude = [ 'created_at', 'updated_at',]
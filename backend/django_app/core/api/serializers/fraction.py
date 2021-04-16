from rest_framework import serializers

# import models
from core.models import Fraction, Membership

class FractionSerializer(serializers.ModelSerializer):
    """
    model serializer for fraction
    """


    number_of_active_members = serializers.SerializerMethodField()

    class Meta:
        model = Fraction
        exclude = ["created_at", "updated_at",]

    def get_number_of_active_members(self, fraction):
        members = Membership.objects.filter(fraction=fraction, end_date__isnull=True)
        return members.count()

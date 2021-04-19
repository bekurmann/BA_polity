from rest_framework import serializers

# import models
from core.models import Fraction, Membership

class FractionSerializer(serializers.ModelSerializer):
    """
    model serializer for fraction
    """


    number_of_active_members = serializers.SerializerMethodField()

    number_of_members_2010 = serializers.SerializerMethodField()
    number_of_members_2014 = serializers.SerializerMethodField()

    class Meta:
        model = Fraction
        exclude = ["created_at", "updated_at",]

    def get_number_of_active_members(self, fraction):
        members = Membership.objects.filter(fraction=fraction, end_date__isnull=True)
        return members.count()

    def get_number_of_members_2010(self, fraction):
        # still active members from 1.1.2010
        members2010_still_active = Membership.objects.filter(fraction=fraction, end_date__isnull=True, start_date__range=["1990-01-01", "2010-07-01"]).count()
        # members start before 1.7.2010; end before today
        members2010_inactive = Membership.objects.filter(fraction=fraction, start_date__range=["1990-01-01", "2010-07-01"], end_date__range=["2010-07-01", "2021-04-19"]).count()

        total = members2010_inactive + members2010_still_active
        return total

    def get_number_of_members_2014(self, fraction):
        # still active members from 1.1.2010
        members2010_still_active = Membership.objects.filter(fraction=fraction, end_date__isnull=True, start_date__range=["1990-01-01", "2014-06-29"]).count()
        # members start before 1.7.2014; end before 2018-06-30
        members2014_2018_inactive = Membership.objects.filter(fraction=fraction, start_date__range=["1990-01-01", "2014-07-30"], end_date__range=["2014-06-29", "2018-07-30"]).count()

        # members start before 1.7.2014; end before today
        members2018_2022_inactive = Membership.objects.filter(fraction=fraction, start_date__range=["1990-01-01", "2014-07-30"], end_date__range=["2018-06-29", "2021-04-19"]).count()

        total = members2010_still_active + members2014_2018_inactive + members2018_2022_inactive
        return total
    

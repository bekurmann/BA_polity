from rest_framework import serializers

# import models
from core.models import Politican, Affair, AffairDebate, Membership

# import additional serializers 
from locations.api.serializers import PLZSerializer
from core.api.serializers import (FractionSerializer, CommissionSerializer, 
                                    AffairDetailSerializer, AffairDebateListSerializer)

# import date
import datetime

class PoliticanListSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
    fractions = FractionSerializer(read_only=True, many=True)

    number_of_submitted_affairs = serializers.SerializerMethodField()
    days_in_parlament = serializers.SerializerMethodField()

    class Meta:
        model = Politican
        exclude = ['profession', 'date_of_birth', 'parlaments',
                    'email', 'website',
                    'location_query', 
                    'parties', 'executives', 'commissions', 'title', 'street1', 
                    'street2', 'phone',]

    def get_number_of_submitted_affairs(self, politican):
        # wrong related name, should be affairs
        return politican.signatories.count()

    def get_days_in_parlament(self, politican):

        days_in_parlament = ''

        start_date = ''
        end_date = ''

        parlament_memberships = Membership.objects.filter(politican=politican, membership_type="PARLA", membership_function="MEMBE")

        for membership in parlament_memberships:
            start_date = membership.start_date
            end_date = membership.end_date

        if(end_date):
            delta = end_date - start_date
            days_in_parlament = delta.days
        else:
            end = datetime.date.today()
            delta = end - start_date
            days_in_parlament = delta.days

        return days_in_parlament
        
        

class PoliticanDetailSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)

    fractions = FractionSerializer(read_only=True, many=True)
    
    commissions = CommissionSerializer(read_only=True, many=True)


    #affair
    affairs = serializers.SerializerMethodField()
    debate_statements = serializers.SerializerMethodField()

    # stats
    number_of_submitted_affairs = serializers.SerializerMethodField()
    number_of_successful_affairs = serializers.SerializerMethodField()
    number_of_debate_statements = serializers.SerializerMethodField()
    number_of_successful_affairs = serializers.SerializerMethodField()
 
    class Meta:
        model = Politican
        exclude = ['location_query', ]

    def get_affairs(self, politican):
        # returns all affairs (nested) where politican is signatory
        affairs = Affair.objects.filter(signatory=politican)
        affairs_serializer = AffairDetailSerializer(affairs, many=True)
        return affairs_serializer.data

    def get_debate_statements(self, politican):
        statements = AffairDebate.objects.filter(politican=politican)
        statements_serializer = AffairDebateListSerializer(statements, many=True)
        return statements_serializer.data

    def get_number_of_submitted_affairs(self, politican):
        # wrong related name, should be affairs
        return politican.signatories.count()

    def get_number_of_successful_affairs(self, politican):
        success = Affair.objects.filter(signatory=politican, accepted=True).count()
        return success
    
    def get_number_of_debate_statements(self, politican):
        return politican.affairdebates.count()    
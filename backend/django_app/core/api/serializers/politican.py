from rest_framework import serializers

# import models
from core.models import Politican, Affair, AffairDebate, Membership

# import additional serializers 
from locations.api.serializers import PLZSerializer
from core.api.serializers import (FractionSerializer, CommissionSerializer, 
                                    AffairDetailSerializer, AffairDebateListSerializer)

# for geo distance
from django.contrib.gis.geos import GEOSGeometry

# import date
import datetime

# ************************************************************
# Jupyter Politican
# ************************************************************
class PoliticanJupyterSerializer(serializers.ModelSerializer):
    """
    LIST OF ALL POLITICANS
    + some infos from other models
    """
    # politican
    city = serializers.CharField(source="city.name", allow_null=True)
    age_in_days = serializers.SerializerMethodField()
    fraction = serializers.SerializerMethodField()
    fraction_id = serializers.SerializerMethodField()
    days_in_parlament = serializers.SerializerMethodField()
    distance_to_parlament = serializers.SerializerMethodField()

    # number of affairs
    number_of_affairs = serializers.SerializerMethodField()

    # debate information
    number_of_debate_statements = serializers.SerializerMethodField()

    
    class Meta:
        model = Politican
        exclude = ['profession', 'parlaments',
                    'email', 'website',
                    'location_query', 
                    'parties', 'executives', 'commissions', 'title', 'street1', 
                    'street2', 'phone',]

    def get_number_of_affairs(self, politican):
        return politican.signatories.count()

    def get_age_in_days(self, politican):
        end_of_analysis = datetime.date(2020, 12, 31)
        # dummy
        birthday_signatory = datetime.date(2020, 12, 31)

        if politican.date_of_birth is not None:
            birthday_signatory = politican.date_of_birth

        delta = end_of_analysis - birthday_signatory

        return delta.days

    def get_fraction(self, politican):
        # return name of fraction membership
        fraction_memberships = Membership.objects.filter(politican=politican, membership_type="FRACT")
        
        fraction_name = "Unknown"

        for fraction_membership in fraction_memberships:
            fraction_name = fraction_membership.fraction.name
        
        return fraction_name

    def get_fraction_id(self, politican):
        # return id of fraction membership
        fraction_memberships = Membership.objects.filter(politican=politican, membership_type="FRACT")
        
        fraction_id = 999

        for fraction_membership in fraction_memberships:
            fraction_id = fraction_membership.fraction.id

        return fraction_id

    def get_days_in_parlament(self, politican):
        # return number of days in parlament from start to affair submission
        days_in_parlament = ''

        start_date = datetime.date(1970, 1, 1) # dummy value for recognizing untrue info
        end_date = datetime.date(2020, 1, 31)

        parlament_memberships = Membership.objects.filter(politican=politican, 
                                                            membership_type="PARLA", 
                                                            membership_function="MEMBE")

        for membership in parlament_memberships:
            start_date = membership.start_date
            if membership.end_date is not None:
                end_date = membership.end_date


        days_in_parlament = end_date - start_date
        return days_in_parlament.days

    def get_distance_to_parlament(self, politican):
        parlament_memberships = Membership.objects.filter(politican=politican, membership_type="PARLA", membership_function="MEMBE")
        parlament = ''
        politican = ''
        distance = ''

        # fuck; still working on it.
        for membership in parlament_memberships:
            parlament = membership.parlament.location
            politican = membership.politican.location

        if parlament is not None and politican is not '':
            if politican is not None:
                parlament = GEOSGeometry(parlament)
                politican = GEOSGeometry(politican)
           
                # * 100 = km
                # 1 km = 1000m -> * 1000
                distance = parlament.distance(politican) * 100 * 1000

        return distance

    def get_number_of_debate_statements(self, politican):
        #all_debate_statements = AffairDebate.objects.filter(politican=politican)
        return politican.affairdebates.count()


# ************************************************************
# Politican 
# ************************************************************
class PoliticanListSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)
    fractions = FractionSerializer(read_only=True, many=True)

    number_of_submitted_affairs = serializers.SerializerMethodField()
    days_in_parlament = serializers.SerializerMethodField()

    distance_to_parlament = serializers.SerializerMethodField()
    
    number_of_debate_statements = serializers.SerializerMethodField()

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

        start_date = datetime.date(2010, 1, 1)
        end_date = ''

        parlament_memberships = Membership.objects.filter(politican=politican, membership_type="PARLA", membership_function="MEMBE")

        for membership in parlament_memberships:
            start_date = membership.start_date
            end_date = membership.end_date

        if(end_date and start_date > datetime.date(2010, 1 ,1)):
            # start date should be 1.1.2010 -> analysis time period 
            delta = end_date - start_date
            days_in_parlament = delta.days
        elif(end_date and start_date < datetime.date(2010, 1, 1)):
            start_special = datetime.date(2010, 1, 1)
            delta = end_date - start_special
            days_in_parlament = delta.days
        else:
            end = datetime.date.today()
            delta = end - start_date
            days_in_parlament = delta.days

        return days_in_parlament

    def get_number_of_debate_statements(self, politican):
        return politican.affairdebates.count()    
        
    def get_distance_to_parlament(self, politican):
        parlament_memberships = Membership.objects.filter(politican=politican, membership_type="PARLA", membership_function="MEMBE")
        parlament = ''
        politican = ''
        distance = ''

        # fuck; still working on it.
        for membership in parlament_memberships:
            parlament = membership.parlament.location
            politican = membership.politican.location

        if parlament is not None and politican is not '':
            if politican is not None:
                parlament = GEOSGeometry(parlament)
                politican = GEOSGeometry(politican)
           
                # * 100 = km
                # 1 km = 1000m -> * 1000
                distance = parlament.distance(politican) * 100 * 1000

        return distance

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
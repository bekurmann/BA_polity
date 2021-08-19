from rest_framework import serializers

# q for filtering
from django.db.models import Q

# import models
from core.models import Affair, AffairDebate, AffairFile, Membership

# for geo distance
from django.contrib.gis.geos import GEOSGeometry

# import date
import datetime

# ************************************************************
# JupyterAffair
# ************************************************************
class AffairJupyterSerializer(serializers.ModelSerializer):
    """
    LIST OF ALL AFFAIRS
    + some infos from other models
    """

    # signatory information
    signatory_first_name = serializers.CharField(source="signatory.first_name", allow_null=True)
    signatory_last_name = serializers.CharField(source="signatory.last_name", allow_null=True)
    signatory_city = serializers.CharField(source="signatory.city.name", allow_null=True)
    signatory_fraction = serializers.SerializerMethodField()
    # strength fraction in percent at time of submission
    signatory_fraction_strength = serializers.SerializerMethodField()
    signatory_days_in_parlament_at_submission = serializers.SerializerMethodField()
    signatory_distance_to_parlament = serializers.SerializerMethodField()

    # vote information
    vote_result_yes_share = serializers.SerializerMethodField()

    # debate information
    number_of_debate_statements = serializers.SerializerMethodField()

    class Meta:
        model = Affair
        exclude = ["created_at", "updated_at", "additional_information", "content_all", 
                    "content_motivation",
                    "content_inquiries", "content_response",
                    "commission", "joint_signatories", "personalised_yes", 
                    "personalised_no", "personalised_abstinence",]
    
    def get_signatory_fraction(self, affair):
        # return name of fraction membership
        fraction_memberships = Membership.objects.filter(politican=affair.signatory, membership_type="FRACT")
        
        fraction_name = "Unknown"

        for fraction_membership in fraction_memberships:
            fraction_name = fraction_membership.fraction.name
        
        return fraction_name

    def get_signatory_days_in_parlament_at_submission(self, affair):
        # return number of days in parlament from start to affair submission
        days_in_parlament_at_submission = ''

        start_date = datetime.date(1970, 1, 1) # dummy value for recognizing untrue info
        end_date = affair.date_received

        parlament_memberships = Membership.objects.filter(politican=affair.signatory, 
                                                            membership_type="PARLA", 
                                                            membership_function="MEMBE")

        for membership in parlament_memberships:
            start_date = membership.start_date


        days_in_parlament_at_submission = end_date - start_date
        return days_in_parlament_at_submission.days

    def get_signatory_fraction_strength(self, affair):
        # returns relative fraction strength

        # find out fraction id
        fraction_memberships = Membership.objects.filter(politican=affair.signatory, membership_type="FRACT")
        fraction_id = 0
        for fraction_membership in fraction_memberships:
            fraction_id = fraction_membership.fraction.id

        # get all members with the same fraction id; active at the time of submission
        # q filtering: model.objects.filter(Q(first_name=foo) | Q(last_name=bar))
        all_fraction_memberships = Membership.objects.filter(
                                                            Q(fraction=fraction_id, 
                                                            membership_type="FRACT",
                                                            start_date__lt=affair.date_received,
                                                            end_date=None,
                                                            ) | Q(
                                                            fraction=fraction_id, 
                                                            membership_type="FRACT",
                                                            start_date__lt=affair.date_received,
                                                            end_date__gt=affair.date_received
                                                            ))

        number_of_fraction_members = all_fraction_memberships.count()
        return number_of_fraction_members

    def get_signatory_distance_to_parlament(self, affair):
        parlament_memberships = Membership.objects.filter(politican=affair.signatory, membership_type="PARLA", membership_function="MEMBE")
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

    def get_vote_result_yes_share(self, affair):
        total_votes = affair.anon_yes + affair.anon_no + affair.anon_abstinence

        if total_votes == 0:
            yes_share = 0
        else:
            yes_votes = affair.anon_yes
            yes_share = yes_votes / total_votes * 100
            
        return yes_share

    def get_number_of_debate_statements(self, affair):
        pass



# ************************************************************
# Affair
# ************************************************************

class AffairListSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (list)
    """

    class Meta:
        model = Affair
        exclude = ["created_at", "updated_at", "additional_information", "content_all", "content_motivation",
                    "content_inquiries", "joint_signatories_count", "anon_yes", "anon_no", "anon_abstinence", 
                    "recommendation", "transformation_recommendation", "content_response", "discussion_desired",
                    "transformation_postulat", "commission", "joint_signatories", "personalised_yes", 
                    "personalised_no", "personalised_abstinence",]

class AffairDetailSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (detail)
    """

    affair_type = serializers.CharField(source='get_affair_type_display')

    class Meta:
        model = Affair
        exclude = ["created_at", "updated_at",]

# ************************************************************
# AffairDebate
# ************************************************************
class AffairDebateListSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (list)
    """
    affair = AffairListSerializer(read_only=True)

    politican_first_name = serializers.SerializerMethodField()
    politican_last_name = serializers.SerializerMethodField()


    class Meta:
        model = AffairDebate
        exclude = ["created_at", "updated_at",]

    def get_politican_first_name(self, debate):
        return debate.politican.first_name

    def get_politican_last_name(self, debate):
        return debate.politican.last_name


class AffairDebateDetailSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (detail) !!! PROBABLY UNNECESSARY -> NESTED
    """

    class Meta:
        model = AffairDebate
        exclude = ["created_at", "updated_at",]
# ************************************************************
# AffairFile
# ************************************************************
class AffairFileListSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (list)
    """

    class Meta:
        model = AffairFile
        exclude = ["created_at", "updated_at",]

class AffairFileDetailSerializer(serializers.ModelSerializer):
    """
    model serializer for affair (list)
    """

    class Meta:
        model = AffairFile
        exclude = ["created_at", "updated_at",]
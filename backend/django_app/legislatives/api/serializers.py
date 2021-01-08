from rest_framework import serializers

from legislatives.models import Parlament, ParlamentRole, ParlamentMembership, ParlamentMembershipRole
from legislatives.models import Commission, CommissionRole, CommissionMembership, CommissionMembershipRole
from locations.api.serializers import PLZSerializer

# *****************************************************************************************
# Parlament
# *****************************************************************************************

class ParlamentSerializer(serializers.ModelSerializer):
    """ 
    model serializer for parlament
        * city is nested with PLZSerializer
        * notice excluded fields
    """
    city = PLZSerializer(read_only=True)

    class Meta:
        model = Parlament
        exclude = ['created_at', 'updated_at', 'location_query']


class ParlamentRoleSerializer(serializers.ModelSerializer):
    """
    model serializer for parlamentrole 
        * used as nested serializer within ParlamentMembershipSerializer
    """
    class Meta:
        model = ParlamentRole
        exclude = ['created_at', 'updated_at',]


class ParlamentMembershipSerializer(serializers.ModelSerializer):
    """
    model serializer for parlament memberships
        * also used in PoliticanSerializer
        * nested ParlamentRoles
    """
    membership_roles = serializers.SerializerMethodField()
    class Meta:
        model = ParlamentMembership
        exclude = [ 'id', 'created_at', 'updated_at',]

    def get_membership_roles(self, object):
        return ParlamentMembershipRoleSerializer(ParlamentMembershipRole.objects.filter(parlament_membership=object), many=True).data



class ParlamentMembershipRoleSerializer(serializers.ModelSerializer):
    """
    model serializer for through model parlamet membership roles
    """
    class Meta:
        model = ParlamentMembershipRole
        exclude = [ 'created_at', 'updated_at', ]












class CommissionSerializer(serializers.ModelSerializer):
    """
    model serializer for commission
    """
    class Meta:
        model = Commission
        exclude = ['created_at', 'updated_at',]
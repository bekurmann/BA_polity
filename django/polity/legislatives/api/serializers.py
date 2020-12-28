from rest_framework import serializers

from legislatives.models import Parlament, ParlamentRole, ParlamentMembership, ParlamentMembershipRole
from legislatives.models import Commission, CommissionRole, CommissionMembership, CommissionMembershipRole
from locations.api.serializers import PLZSerializer

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

    # def get_commissions = 


class ParlamentRoleSerializer(serializers.ModelSerializer):
    """
    model serializer for parlamentrole 
        * used as nested serializer within ParlamentMembershipSerializer
    """
    class Meta:
        model = ParlamentRole
        exclude = ['id', 'created_at', 'updated_at', 'description',]

class ParlamentMembershipSerializer(serializers.ModelSerializer):
    """
    model serializer for parlament memberships
        * also used in PoliticanSerializer
        * nested ParlamentRoles
    """
    membership_roles = ParlamentRoleSerializer(many=True, read_only=True)
    class Meta:
        model = ParlamentMembership
        exclude = ['id', 'created_at', 'updated_at', ]

class CommissionSerializer(serializers.ModelSerializer):
    """
    model serializer for commission
    """
    class Meta:
        model = Commission
        exclude = ['created_at', 'updated_at',]
from rest_framework import serializers

from politicans.models import Politican

# imports for parlament memberships
from legislatives.models import ParlamentMembership
from legislatives.api.serializers import ParlamentMembershipSerializer

# import for field city -> bfs_nummer -> municipality GIS
from locations.api.serializers import PLZSerializer

class PoliticanSerializer(serializers.ModelSerializer):
    city = PLZSerializer(read_only=True)

    membership_parlaments = serializers.SerializerMethodField()
   
    class Meta:
        model = Politican
        exclude = ['created_at', 'updated_at', 'location_query', ]

    def get_membership_parlaments(self, object):
        # returns a serialized .data where politican is parlament member
        return ParlamentMembershipSerializer(ParlamentMembership.objects.filter(politican=object), 
                                                many=True).data

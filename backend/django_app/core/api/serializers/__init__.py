from rest_framework import serializers

# import models
from core.models import (   Politican, Party, Parlament, Commission,
                            Fraction, AffairTopic, Affair, Session,
                            Membership )

# import location app serializers
from locations.api.serializers import PLZSerializer, CantonNestedSerializer

from .politican import PoliticanSerializer
# from .party import 
from .parlament import ParlamentSerializer
from .commission import CommissionSerializer
#from .fraction import 
#from .affair import
#from .session import 
from .membership import MembershipSerializer 
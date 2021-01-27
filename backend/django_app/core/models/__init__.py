from django.db import models

# for location
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
# import locations
from locations.models import Country, Canton, Municipality, PLZ

from .politican import Politican
from .party import Party
from .parlament import Parlament
from .commission import Commission
from .fraction import Fraction
from .affair import Affair, AffairTopic
from .session import Session
from .membership import Membership





    







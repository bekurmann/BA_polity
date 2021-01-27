from django.contrib import admin

# import models
from core.models import (   Politican, Party, Parlament, Commission,
                            Fraction, AffairTopic, Affair, Session,
                            Membership )

from locations.models import Country, Canton, Municipality, PLZ

# avatar preview
from django.utils.safestring import mark_safe

# import export 
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from .politican import PoliticanAdmin
from .party import PartyAdmin
from .parlament import ParlamentAdmin
from .commission import CommissionAdmin
from .fraction import FractionAdmin
# from .affair import 
from .session import SessionAdmin
from .membership import MembershipAdmin
# from .party import 
from .parlament import ParlamentListSerializer, ParlamentDetailSerializer
from .commission import CommissionSerializer
from .fraction import FractionSerializer
from .affair import ( AffairListSerializer, AffairDetailSerializer,
                    AffairDebateListSerializer, AffairDebateDetailSerializer,
                    AffairFileListSerializer, AffairFileDetailSerializer )
from .session import SessionSerializer
# need to be down here because of import order
from .politican import PoliticanListSerializer, PoliticanDetailSerializer
from .membership import MembershipListSerializer, MembershipDetailSerializer 
#from .analysis import 
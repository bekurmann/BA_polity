from django.db import models

from location_field.models.spatial import LocationField

from politicans.models import Politican
from locations.models import Country, Canton, Municipality, PLZ


# *****************************************************************************************
# Parlament
# *****************************************************************************************
class Parlament(models.Model):
    """
    * model for parlaments
    
    please note:
    * fk jurisdiction for geo data of canton
        -> sparse, depending on administrative level
    * fk city for plz / bfs_nummer -> municipality (address)
    """

    # general information
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    number_of_seats = models.IntegerField(blank=True, null=True)
    
    # fk for geodata 
    # sparse model, depending on administrative level (federal, canton, municipality)
    jurisdiction_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_parlaments", blank=True, null=True)
    jurisdiction_canton = models.ForeignKey(Canton, on_delete=models.CASCADE, related_name="canton_parlaments", blank=True, null=True)
    jurisdiction_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name="municipality_parlaments", blank=True, null=True)

    # manytomany members
    members = models.ManyToManyField(Politican, through='Membership',
                                                through_fields=('parlament',
                                                'politican'))

    # address
    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(PLZ, on_delete=models.CASCADE, related_name="parlaments", blank=True, null=True)

    # location
    location_query = models.CharField(max_length=200, blank=True, null=True)
    location = LocationField(based_fields=['location_query'], zoom=7, blank=True, null=True)

    # contact
    email = models.EmailField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    # avatar
    def get_parlament_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/legislatives/parlaments/<title>_<city.name>/<filename>
        return f'legislatives/parlaments/{instance.title}_{instance.city.name}/{filename}'
    avatar = models.ImageField(upload_to=get_parlament_upload_path, blank=True, null=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

class ParlamentSession(models.Model):
    """
    model for parlament sessions
    """
    # fk parlament
    parlament = models.ForeignKey(Parlament, on_delete=models.CASCADE, related_name='parlament_sessions')

    # general information
    date = models.DateField()
    opening_session = models.BooleanField()
    regular_session = models.BooleanField()
    additional_information = models.TextField(blank=True)

    # greeting / address of discharge
    greeting = models.TextField(blank=True)
    discharge = models.TextField(blank=True)

    # TODO :manytomany affairs
    #affairs = models.ManyToManyField()

    # manytomany politicans
    excused_politicans = models.ManyToManyField(Politican, blank=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date}'
    

# *****************************************************************************************
# Commission
# *****************************************************************************************
class Commission(models.Model):
    """
    * model for commissions
    """
    # general information
    title = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    # fk for parlament
    parlament = models.ForeignKey(Parlament, on_delete=models.CASCADE, related_name="commissions")

    # members
    members = models.ManyToManyField(Politican, through='Membership',
                                                through_fields=('commission',
                                                'politican'))

    # permanent / non-permanent commission | start/end date
    permanent = models.BooleanField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    # contact
    email = models.EmailField( max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    # avatar
    def get_commission_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/legislatives/parlaments/<title>_<city.name>/<filename>
        return f'legislatives/parlaments/commissions/{instance.title}/{filename}'
    avatar = models.ImageField(upload_to=get_commission_upload_path, blank=True, null=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

# class CommissionMembership(models.Model):
#     """
#     through model for manytomany politican - commission
#     """
#     # type
#     MEMBER = 'MEMBE'
#     PRESIDENT = 'PRESI'
#     VICEPRESIDENT = 'VICEP'
#     TYPE_CHOICES = [
#         (MEMBER, 'Member'),
#         (PRESIDENT, 'President'),
#         (VICEPRESIDENT, 'Vice-President')
#     ]
#     membership_type = models.CharField(max_length=5, choices=TYPE_CHOICES, default=MEMBER)

#     # fk
#     politican = models.ForeignKey(Politican, on_delete=models.CASCADE)
#     commission = models.ForeignKey(Commission, on_delete=models.CASCADE)

#     # start & end date
#     start_date = models.DateField()
#     end_date = models.DateField(blank=True, null=True)

#     # TODO: fk election? or how do you become commission member?

#     # admin
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         constraints = [
#             # membership type of one politican must be unique for one commission
#             models.UniqueConstraint(fields=['membership_type', 'commission'], name='unique_commission_membership_types')
#         ]

#     # calculated active flag
#     def active(self):
#         "Returns whether or not the Membership is active, depending on end_date"
#         import datetime
#         if not self.end_date:
#             # if end_date not set, membership true
#             return True
#         elif self.end_date > datetime.date.today():
#             # if end_date set, but in future, membership true
#             return True
#         return False
#     active.boolean = True

#     def __str__(self):
#         return f'{self.politican.first_name} {self.politican.last_name} / {self.commission.title}'

# *****************************************************************************************
# Membership
# *****************************************************************************************
class Membership(models.Model):
    """
    sparse model for membersips
    * used for
        parlament
        commission
        fraction
     as through model
    """
    # membership type
    PARLAMENT = 'PARLA'
    COMMISSION = 'COMMI'
    FRACTION = 'FRACT'
    TYPE_CHOICES = [
        (PARLAMENT, 'Parlament'),
        (COMMISSION, 'Commission'),
        (FRACTION, 'Fraction')
    ]
    membership_type = models.CharField(max_length=5, choices=TYPE_CHOICES)

    # membership function
    MEMBER = 'MEMBE'
    PRESIDENT = 'PRESI'
    VICEPRESIDENT = 'VICEP'
    VOTECOUNTER = 'VOTEC'
    SECRETARY = 'SECRE'
    FUNCTION_CHOICES = [
        (MEMBER, 'Member'),
        (PRESIDENT, 'President'),
        (VICEPRESIDENT, 'Vice-President'),
        (VOTECOUNTER, 'Vote Counter'),
        (SECRETARY, 'Secretary')
    ]
    membership_function = models.CharField(max_length=5, choices=FUNCTION_CHOICES, default=MEMBER)

    #fk 
    politican = models.ForeignKey(Politican, on_delete=models.CASCADE)
    parlament = models.ForeignKey(Parlament, on_delete=models.CASCADE, blank=True, null=True)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, blank=True, null=True)
    #fraction = models.ForeignKey()

    # start & end date
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # TODO: reference election

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            # membership type of one politican must be unique for one parlament
            models.UniqueConstraint(fields=['membership_type', 'membership_function', 'politican'], name='unique_parlament_membership_types'),
        ]

    # calculated active flag
    def active(self):
        # Returns whether or not the Membership is active, depending on end_date
        import datetime
        if not self.end_date:
            # if end_date not set, membership true
            return True
        elif self.end_date > datetime.date.today():
            # if end_date set, but in future, membership true
            return True
        return False
    active.boolean = True

    def __str__(self):
        return f'{self.politican.first_name} {self.politican.last_name} / {self.membership_type} / {self.membership_function}'

# *****************************************************************************************
# Affairs
# *****************************************************************************************

class AffairTopic(models.Model):
    """
    model for topics
    * based on the topics of curavista, federal parlament
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

class Affair(models.Model):
    """
    base model affairs
    * manytomany field to topic
    * manytomany field to session
    """
    # type choices
    INQUIRY = 'INQUI'               # Anfrage/Kleine Anfrage/Fragestunde
    INTERPELLATION = 'INTER'        # Interpellation
    POSTULATE = 'POSTU'             # Postulat
    MOTION = 'MOTIO'                # Motion
    LEGISLATIVEPROPOSAL = 'LEGIS'   # Gesetzgebungsvorlage (Kommission)
    TYPE_CHOICES = [
        (INQUIRY, 'Inquiry'),
        (INTERPELLATION, 'Interpellation'),
        (POSTULATE, 'Postulate'),
        (MOTION, 'Motion'),
        (LEGISLATIVEPROPOSAL, 'Legislative Proposal')
    ]
    # status choices
    UNKNOWN = 'UNKNO'
    RECEIVED = 'RECEI'
    TRANSFERED = 'TRANS'
    ANSWERED = 'ANSWE'
    PROCESSED = 'PROCE'
    STATUS_CHOICES = [
        (UNKNOWN, 'Unknown'),
        (RECEIVED, 'Received'),
        (TRANSFERED, 'Transfered'),
        (ANSWERED, 'Answered'),
        (PROCESSED, 'Processed')
    ]

    # general information
    affiar_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default=UNKNOWN)
    urgent = models.BooleanField(blank=True)
    identifier = models.CharField(max_length=200)
    date_received = models.DateField()
    # authorship
    signatory = models.ForeignKey(Politican, on_delete=models.CASCADE, related_name="inquiry_signatories")
    joint_signatory = models.ManyToManyField(Politican, related_name="inquiry_joint_signatories", blank=True)
    # topics
    topics = models.ManyToManyField(AffairTopic, related_name="affair_topics", blank=True)

    # content
    content_all = models.TextField(blank=True)
    content_motivation = models.TextField(blank=True)
    content_inquiries = models.TextField(blank=True)

    # executive statement


    # sessions
    sessions = models.ManyToManyField(ParlamentSession, related_name="affair_sessions", blank=True)

    # debates
    # TODO: many to many debates

    # *****************************************
    # special fields for Legislative Proposal
    # *****************************************
    # applications (anträge; only legislativeproposals have applications (one to many))
    # dispatch (botschaft)
    # consultation (vernehmlassung)
    # legislative proposal (gesetzesvorlage)
    # regulatory statuses (ausführungsbestimmungen)
    # *****************************************


    # social??? -> still to do

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.identifier} {self.date_received}'
    
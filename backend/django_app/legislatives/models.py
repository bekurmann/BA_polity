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
    members = models.ManyToManyField(Politican, through='ParlamentMembership',
                                                through_fields=('parlament',
                                                'politican'))

    # address
    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(PLZ, on_delete=models.CASCADE, related_name="parlaments", blank=True, null=True)

    # location
    location_query = models.CharField(max_length=200, blank=True, null=True)
    location = LocationField(based_fields=['street1', 'street2', 'location_query'], zoom=7, blank=True, null=True)

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

    # manytomany affairs
    # TODO
    #affairs = models.ManyToManyField()

    # manytomany politicans
    excused_politicans = models.ManyToManyField(Politican, blank=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date}'
    

class ParlamentRole(models.Model):
    """
    model for roles inside a parlament
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # fk parlament
    parlament = models.ForeignKey(Parlament, on_delete=models.CASCADE, related_name="parlament_roles")

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'parlament'], name='unique_parlament_roles')
        ]

    def __str__(self):
        return f'{self.title} {self.parlament.title}'

class ParlamentMembership(models.Model):
    """
    * through model for manytomany politican - parlament
    """
    politican = models.ForeignKey(Politican, on_delete=models.CASCADE)
    parlament = models.ForeignKey(Parlament, on_delete=models.CASCADE)

    membership_roles = models.ManyToManyField(ParlamentRole,
                                                through='ParlamentMembershipRole',
                                                through_fields=('parlament_membership',
                                                'parlament_role'))

    # start & end date
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # active flag  -> TODO: computed?
    active = models.BooleanField()

    # TODO: reference election

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            # one politican can only be member of the same parlament once
            models.UniqueConstraint(fields=['politican', 'parlament'], name='unique_parlament_memberships')
        ]

    def __str__(self):
        return f'{self.politican.first_name} {self.politican.last_name} / {self.parlament.title}'

class ParlamentMembershipRole(models.Model):
    """
    * through model for through model ParlamentMembership manytomany membership_roles
    """
    parlament_membership = models.ForeignKey(ParlamentMembership, on_delete=models.CASCADE)
    parlament_role = models.ForeignKey(ParlamentRole, on_delete=models.CASCADE)

    # additional date information
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # reference election
    # TO DO -> !

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            # one politican can only be member of the same parlament once
            models.UniqueConstraint(fields=['parlament_membership', 'parlament_role'], name='unique_parlament_membership_roles')
        ]

    def __str__(self):
        return f'{self.parlament_role.title}'

# *****************************************************************************************
# Commission
# *****************************************************************************************
class Commission(models.Model):
    """
    * model for commissions
    """
    # general information
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # fk for parlament
    parlament = models.ForeignKey(Parlament, on_delete=models.CASCADE, related_name="commissions")

    # members
    members = models.ManyToManyField(Politican, through='CommissionMembership',
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

class CommissionRole(models.Model):
    """ 
    model for roles inside a commission
    """
    title = models.CharField(max_length=200)

    # fk commission
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name="commission_roles")

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'commission'], name='unique_commission_roles')
        ]

    def __str__(self):
        return f'{self.title} {self.commission.title}'

class CommissionMembership(models.Model):
    """
    through model for manytomany politican - commission
    """
    politican = models.ForeignKey(Politican, on_delete=models.CASCADE)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)

    membership_roles = models.ManyToManyField(CommissionRole,
                                                through='CommissionMembershipRole',
                                                through_fields=('commission_membership',
                                                'commission_role'))

    # start & end date
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # active flag; computed=
    active = models.BooleanField()

    # TODO: election? or how do you become commission member?

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            # one politican can only be member of the same commission once
            models.UniqueConstraint(fields=['politican', 'commission'], name='unique_commission_memberships')
        ]

    def __str__(self):
        return f'{self.politican.first_name} {self.politican.last_name} / {self.commission.title}'

class CommissionMembershipRole(models.Model):
    """
    through model for through model CommissionMembership manytomany membership_roles
    """
    commission_membership = models.ForeignKey(CommissionMembership, on_delete=models.CASCADE)
    commission_role = models.ForeignKey(CommissionRole, on_delete=models.CASCADE)

    # additional date information
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # reference election
    # TO DO -> !

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.commission_role.title}'

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
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default=UNKNOWN)
    urgent = models.BooleanField(blank=True)
    identifier = models.CharField(max_length=200)
    date_received = models.DateField()
    
    # topics
    topics = models.ManyToManyField(AffairTopic, related_name="affair_topics", blank=True)

    # executive statement


    # sessions
    sessions = models.ManyToManyField(ParlamentSession, related_name="affair_sessions", blank=True)

    # debates
    # TODO: many to many debates

    # social??? -> still to do

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.identifier} {self.date_received}'
    

class Inquiry(Affair):
    """
    model for inquiry (* DE: anfragen / kleine anfragen / einfach anfragen)
    * inherits from affair
    * signatory + joint_signatory refers to politican
    """
    # signatory
    signatory = models.ForeignKey(Politican, on_delete=models.CASCADE, related_name="inquiry_signatories")
    joint_signatory = models.ManyToManyField(Politican, related_name="inquiry_joint_signatories", blank=True)

    # content
    # motivation
    content_motivation = models.TextField(blank=True)
    content_inquiries = models.TextField(blank=True)


    # questions
    # many to many questions

    # response executive

class Interpellation(Affair):
    pass

class Postulate(Affair):
    pass

class Motion(Affair):
    pass

class Legislation(Affair):
    # gesetzgebungsvorlage
    pass
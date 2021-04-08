from django.db import models

# *****************************************************************************************
# Affairs
# *****************************************************************************************

class Affair(models.Model):
    """
    model for affair
    """
    # type choices
    INQUIRY = 'INQUI'             
    INTERPELLATION = 'INTER'   
    POSTULATE = 'POSTU'         
    MOTION = 'MOTIO'    
    PEOPLE_MOTION = 'PMOTI'          
    LEGISLATIVEPROPOSAL = 'LEGIS'  # gesetzgebungsvorlage
    TYPE_CHOICES = [
        (INQUIRY, 'Inquiry'),
        (INTERPELLATION, 'Interpellation'),
        (POSTULATE, 'Postulate'),
        (MOTION, 'Motion'),
        (PEOPLE_MOTION, 'People Motion'),
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

    # #######################################################################
    # general information
    # #######################################################################
    title = models.CharField(max_length=200)
    affair_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default=UNKNOWN)
    urgent = models.BooleanField(blank=True)
    identifier = models.CharField(max_length=200)
    parlament = models.ForeignKey('core.Parlament', on_delete=models.CASCADE, related_name="affairs_parlaments", blank=True, null=True)
    date_received = models.DateField()
    additional_information = models.TextField(blank=True)

    # topics
    topics = models.ManyToManyField('core.Topic', related_name="affairs_topics", blank=True)

    # content
    content_all = models.TextField(blank=True)
    content_motivation = models.TextField(blank=True)
    content_inquiries = models.TextField(blank=True)

    # sessions
    session = models.ForeignKey('core.Session', on_delete=models.CASCADE, related_name="affairs_sessions", blank=True, null=True)

    # #######################################################################
    # authorship
    # #######################################################################
    signatory = models.ForeignKey('core.Politican', on_delete=models.CASCADE, related_name="signatories", blank=True, null=True)
    joint_signatories = models.ManyToManyField('core.Politican', related_name="joint_signatories", blank=True)
    joint_signatories_count = models.IntegerField()
    # if not politican is signatory, but a commission
    commission = models.ForeignKey('core.Commission', on_delete=models.CASCADE, related_name="commissions", blank=True, null=True)

    # #######################################################################
    # vote
    # #######################################################################
    # anon vote
    anon_yes = models.IntegerField(blank=True)
    anon_no = models.IntegerField(blank=True)
    anon_abstinence = models.IntegerField(blank=True)

    # personalised vote
    personalised_yes = models.ManyToManyField('core.Politican', related_name="affair_yeses", blank=True)
    personalised_no = models.ManyToManyField('core.Politican', related_name="affair_nos", blank=True)
    personalised_abstinence = models.ManyToManyField('core.Politican', related_name="affair_abstinences", blank=True)

    # motion / postulat accepted (more yes than no, maybe computed?)
    accepted = models.BooleanField(blank=True)

    # #######################################################################
    # statement executive
    # #######################################################################

    # recommendation executive accept/not accept
    recommendation = models.BooleanField(blank=True)
    # recommendation executive transformation motion -> postulat
    transformation_recommendation = models.BooleanField(blank=True)

    content_response = models.TextField(blank=True)

    # #######################################################################
    # special variables
    # #######################################################################
    # interpellation
    discussion_desired = models.BooleanField(blank=True)
    # motion
    transformation_postulat = models.BooleanField(blank=True)

    # social??? -> still to do

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.identifier} {self.title}'

class AffairDebate(models.Model):
    """
    model for affair debate
    * statements made in parlamet regarding the affair, WORTMELDUNGEN
    """
    session = models.ForeignKey('core.Session', on_delete=models.CASCADE, related_name="affairdebates", blank=True, null=True)
    affair = models.ForeignKey('core.Affair', on_delete=models.CASCADE, related_name="affairdebates", blank=True, null=True)
    politican = models.ForeignKey('core.Politican', on_delete=models.CASCADE, related_name="affairdebates", blank=True, null=True)

    order = models.IntegerField()

    content = models.TextField(blank=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.politican.first_name} {self.politican.last_name} {self.affair.title}'
    
    
class AffairFile(models.Model):
    """
    model for affair files (not protocols, only files related to affair)
    """
    affair = models.ForeignKey('core.Affair', on_delete=models.CASCADE, related_name="affairs")

    def get_affair_file_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/affairs/<parlament.name>/<identifier>/<filename>
        return f'affairs/{instance.affair.parlament.name}/{instance.affair.identifier}/{filename}'

    # default file length is 100; not enough!
    affair_file = models.FileField(upload_to=get_affair_file_upload_path, max_length=600)
    
    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.affair.title}'
from django.db import models

# *****************************************************************************************
# Affairs
# *****************************************************************************************

class Affair(models.Model):
    """
    base model affairs
    * manytomany field to topic
    * manytomany field to session
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

    # general information
    title = models.CharField(max_length=200)
    affair_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default=UNKNOWN)
    urgent = models.BooleanField(blank=True)
    identifier = models.CharField(max_length=200)
    parlament = models.ForeignKey('core.Parlament', on_delete=models.CASCADE, related_name="parlaments", blank=True, null=True)
    date_received = models.DateField()

    # authorship
    signatory = models.ForeignKey('core.Politican', on_delete=models.CASCADE, related_name="signatories")
    joint_signatories = models.ManyToManyField('core.Politican', related_name="joint_signatories", blank=True)
    joint_signatories_count = models.IntegerField()
    # topics

    topics = models.ManyToManyField('core.Topic', related_name="topics", blank=True)

    # content
    content_all = models.TextField(blank=True)
    content_motivation = models.TextField(blank=True)
    content_inquiries = models.TextField(blank=True)

    # sessions
    sessions = models.ManyToManyField('core.Session', related_name="sessions", blank=True)

    # #######################################################################
    # vote
    # #######################################################################
    # anon vote
    anon_yes = models.IntegerField()
    anon_no = models.IntegerField()
    anon_abstinence = models.IntegerField()

    # personalised vote
    personalised_yes = models.ManyToManyField('core.Politican', on_delete=models.CASCADE, related_name=affair_yeses, blank=True, null=True)
    personalised_no = models.ManyToManyField('core.Politican', on_delete=models.CASCADE, related_name=affair_nos, blank=True, null=True)
    personalised_abstinence = models.ManyToManyField('core.Politican', on_delete=models.CASCADE, related_name=affair_abstinences, blank=True, null=True)


    # social??? -> still to do

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.identifier} {self.title}'
    
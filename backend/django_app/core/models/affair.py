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
    
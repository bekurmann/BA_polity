from django.db import models

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
    PARTY = 'PARTY'
    EXECUTIVE = 'EXECU'
    TYPE_CHOICES = [
        (PARLAMENT, 'Parlament'),
        (COMMISSION, 'Commission'),
        (FRACTION, 'Fraction'),
        (PARTY, 'Party'),
        (EXECUTIVE, 'Executive')
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
    politican = models.ForeignKey('core.Politican', on_delete=models.CASCADE, related_name="politican_memberships")
    parlament = models.ForeignKey('core.Parlament', on_delete=models.CASCADE, blank=True, null=True, related_name="parlament_memberships")
    commission = models.ForeignKey('core.Commission', on_delete=models.CASCADE, blank=True, null=True)
    fraction = models.ForeignKey('core.Fraction', on_delete=models.CASCADE, blank=True, null=True)
    party = models.ForeignKey('core.Party', on_delete=models.CASCADE, blank=True, null=True)
    executive = models.ForeignKey('core.Executive', on_delete=models.CASCADE, blank=True, null=True)

    # start & end date
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # TODO: reference election

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     constraints = [
    #         # membership type of one politican must be unique for one parlament 
    #         # not sure if this works with more than one votecounter membership -> true that
    #         models.UniqueConstraint(fields=['membership_type', 'membership_function', 'politican'], name='unique_parlament_membership_types'),
    #     ]

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

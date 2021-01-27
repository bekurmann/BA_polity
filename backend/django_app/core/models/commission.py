from django.db import models

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
    parlament = models.ForeignKey('core.Parlament', on_delete=models.CASCADE, related_name="commissions")

    # members
    members = models.ManyToManyField('core.Politican', through='Membership',
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
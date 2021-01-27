# *****************************************************************************************
# Fraction
# *****************************************************************************************
class Fraction(models.Model):
    """
    * model for fraction
    """
    # general information
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    # fk for parlament
    parlament = models.ForeignKey(Parlament, on_delete=models.CASCADE, related_name="fractions")

    # fk party
    party = models.ForeignKey(Party, on_delete=models.CASCADE, blank=True, null=True)

    # members
    members = models.ManyToManyField(Politican, through='Membership',
                                                through_fields=('fraction',
                                                'politican'))
    
    # address
    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(PLZ, on_delete=models.CASCADE, related_name="fractions")

    # contact
    email = models.EmailField( max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    # avatar
    def get_fraction_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/legislatives/parlaments/<title>_<city.name>/<filename>
        return f'legislatives/parlaments/fractions/{instance.name}/{filename}'
    avatar = models.ImageField(upload_to=get_fraction_upload_path, blank=True, null=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
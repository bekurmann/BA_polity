# *****************************************************************************************
# Party
# *****************************************************************************************

class Party(models.Model):
    """
    model for parties
    """
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    # parent for sections
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    # address
    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(PLZ, on_delete=models.CASCADE, related_name="parties", blank=True, null=True)

    # location
    location_query = models.CharField(max_length=200, blank=True, null=True)
    location = LocationField(based_fields=['location_query'], zoom=7, blank=True, null=True)

    # contact
    email = models.EmailField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    # avatar
    def get_party_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/legislatives/parlaments/<title>_<city.name>/<filename>
        return f'parties/{instance.name}_{instance.city.name}/{filename}'
    avatar = models.ImageField(upload_to=get_party_upload_path, blank=True, null=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.abbreviation}'
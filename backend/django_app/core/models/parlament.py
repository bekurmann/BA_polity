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
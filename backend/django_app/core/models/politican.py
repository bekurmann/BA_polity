from django.db import models

# for location
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

# import locations
from locations.models import Country, Canton, Municipality, PLZ

class Politican(models.Model):
    """
    * model for politican
    * fk city refers to model PLZ (with bfs_nummer also municipality, etc)
    * still todo: 
        - prepopulate location_query with city.name ?
    """

    # personal information
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    profession = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # address
    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(PLZ, on_delete=models.CASCADE, related_name="politicans")

    # location
    location_query = models.CharField(max_length=200, blank=True, null=True)
    location = LocationField(based_fields=['location_query'], zoom=7, blank=True, null=True)

    # memberships
    parlaments = models.ManyToManyField('core.Parlament', through='Membership',
                                                through_fields=('politican',
                                                'parlament'))
    fractions = models.ManyToManyField('core.Fraction', through='Membership',
                                                through_fields=('politican',
                                                'fraction'))
    commissions = models.ManyToManyField('core.Commission', through='Membership',
                                                through_fields=('politican',
                                                'commission'))
    parties = models.ManyToManyField('core.Party', through='Membership',
                                                through_fields=('politican',
                                                'party'))

    # contact
    email = models.EmailField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    # avatar
    def get_politican_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/politicans/<first_name>_<last_name>_<city.name>/<filename>
        return f'politicans/{instance.first_name}_{instance.last_name}_{instance.city.name}/{filename}'

    avatar = models.ImageField(upload_to=get_politican_upload_path, blank=True, null=True)

    # Admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.city.name}'


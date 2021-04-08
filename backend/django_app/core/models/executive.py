from django.db import models

# for location
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
# import locations
from locations.models import Country, Canton, Municipality, PLZ

# *****************************************************************************************
# Executive
# *****************************************************************************************

class Executive(models.Model):
    """
    * model for executive
    """
    # general information
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    number_of_seats = models.IntegerField(blank=True, null=True)

    # fk for geodata 
    # sparse model, depending on administrative level (federal, canton, municipality)
    jurisdiction_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_executives", blank=True, null=True)
    jurisdiction_canton = models.ForeignKey(Canton, on_delete=models.CASCADE, related_name="canton_executives", blank=True, null=True)
    jurisdiction_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name="municipality_executives", blank=True, null=True)

    # address
    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(PLZ, on_delete=models.CASCADE, related_name="executives", blank=True, null=True)

    # location
    location_query = models.CharField(max_length=200, blank=True, null=True)
    location = LocationField(based_fields=['location_query'], zoom=7, blank=True, null=True)

    # contact
    email = models.EmailField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    # avatar
    def get_parlament_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/executives/<title>_<city.name>/<filename>
        return f'executives/{instance.title}_{instance.city.name}/{filename}'
    avatar = models.ImageField(upload_to=get_parlament_upload_path, blank=True, null=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
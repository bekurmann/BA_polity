from django.contrib.auth.models import AbstractUser
from django.db import models

# for location
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

# for get user canton
from locations.models import Canton

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom User Model
    + adds several personal information fields
    + location field (for geo information)
    """

    bio = models.CharField(blank=True, max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    website = models.CharField(blank=True, max_length=50)

    # location
    location_query = models.CharField(max_length=200, blank=True, null=True)
    location = LocationField(based_fields=['location_query'], zoom=7, blank=True, null=True)

    # avatar
    def get_user_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/users/<pk>_<username>/<filename>
        return f'users/{instance.pk}_{instance.username}/{filename}'
    avatar = models.ImageField(upload_to=get_user_upload_path, blank=True, null=True)

    def __str__(self):
        return f'{self.username} {self.email}'
from django.db import models

class Party(models.Model):
    """
    Model Party - displaying party related information 
    + parent for showing sections
    """
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='parties', blank=True, null=True)

    # parent for sections
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    # location
    #location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.abbreviation}'

class PartyFunction(models.Model):
    """
    PartyFunction Model - defining available functions for council
    """

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
from django.db import models

class Session(models.Model):
    """
    model for sessions
    """
    # fk parlament
    parlament = models.ForeignKey('core.Parlament', on_delete=models.CASCADE, related_name='sessions')
    # more fk to come

    # general information
    start_date = models.DateField()
    end_date = models.DateField()
    opening_session = models.BooleanField()
    regular_session = models.BooleanField()
    additional_information = models.TextField(blank=True)

    # greeting / address of discharge
    greeting = models.TextField(blank=True)
    discharge = models.TextField(blank=True)

    # TODO :manytomany affairs
    #affairs = models.ManyToManyField()

    # manytomany politicans
    excused_politicans = models.ManyToManyField('core.Politican', blank=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date}'
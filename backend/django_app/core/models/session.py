from django.db import models

class Session(models.Model):
    """
    model for sessions
    """
    # fk parlament
    parlament = models.ForeignKey('core.Parlament', on_delete=models.CASCADE, related_name='parlaments')
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

    # manytomany politicans
    excused_politicans = models.ManyToManyField('core.Politican', blank=True)

    #files
    def get_word_protocol_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/sessions/protocols/<parlament.title>/<start_date>/<filename>
        return f'sessions/protocls/{instance.parlament.title}/{instance.start_date}/{filename}'

    word_protocol = models.FileField(upload_to=get_word_protocol_upload_path, blank=True, null=True)
    #short_protocol =
    #agenda_items = 

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date} {self.parlament.title}'

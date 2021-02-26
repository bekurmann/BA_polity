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

    # manytomany politicans
    excused_politicans = models.ManyToManyField('core.Politican', blank=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date}'

class SessionFile(models.Model):
    """
    model for session files -> mostly protocols
    """
    session = models.ForeignKey('core.Session', on_delete=models.CASCADE, related_name="sessions")

    def get_session_file_upload_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/sessions/<parlament.name>/<filename>
        return f'sessions/{instance.session.parlament.name}/{instance.session.start_date}/{filename}'

    session_file = models.FileField(upload_to=get_session_file_upload_path)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.session.start_date}'
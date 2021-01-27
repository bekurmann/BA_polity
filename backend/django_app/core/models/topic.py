from django.db import models

class Topic(models.Model):
    """
    model for topics
    * based on the topics of curavista, federal parlament
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
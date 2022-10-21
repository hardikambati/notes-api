from email.policy import default
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Note(models.Model):

    title = models.CharField(max_length=250, blank=False)
    text = models.TextField(blank=False)
    date = models.DateTimeField(default=now)
    starred = models.BooleanField(default=False)

    def __str__(self):
        return self.title
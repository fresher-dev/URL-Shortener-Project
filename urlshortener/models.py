from django.db import models
from django.utils import timezone


class Question(models.Model):
    original_url = models.CharField(max_length=254)
    hash = models.CharField(max_length=10)
    creation_date = models.DateTimeField(default=timezone.now)

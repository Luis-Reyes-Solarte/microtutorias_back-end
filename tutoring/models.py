# Create your models here.
from django.conf import settings
from django.db import models


class TutoringAd(models.Model):
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.ForeignKey("subjects.Subject", on_delete=models.CASCADE)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    available_date = models.DateTimeField()

# Create your models here.
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    experience = models.CharField(max_length=50)
    apply_link = models.URLField()

    def __str__(self):
        return self.title

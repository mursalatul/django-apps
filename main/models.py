from django.db import models

# Create your models here.
class AllApps(models.Model):
    app_name = models.CharField(max_length=100)
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Container(models.Model):
    id = models.AutoField(primary_key=True)
    file_field = models.FileField(null=True)

from django.db import models

# Create your models here.
class Things(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    quantity = models.IntegerField()
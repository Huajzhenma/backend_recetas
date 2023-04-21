from django.db import models

# Create your models here.
class Cocina(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    
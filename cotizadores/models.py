from django.db import models

# Create your models here.

class TR(models.Model):
    Age = models.IntegerField()
    tf = models.DecimalField(max_digits=30, decimal_places=25)

    
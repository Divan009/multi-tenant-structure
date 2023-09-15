from django.db import models

# Create your models here.

class AdditionResult(models.Model):
    answer = models.IntegerField(default=0)

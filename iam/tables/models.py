from django.db import models

# Create your models here.
class DNISTable(models.Model):
    dnis=models.CharField(max_length=20, unique=True)
    queue=models.CharField(max_length=30)
    play_welcome=models.BooleanField()
    prio=models.IntegerField()


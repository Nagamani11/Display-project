from django.db import models
class DisplayData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    qualification = models.CharField(max_length=50)
    percentage = models.IntegerField()
    location = models.CharField(max_length=50)

from django.db import models


# Create your models here.
class ApplicationForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    qulification = models.TextField()
    resume = models.FileField()
    status = models.BooleanField()

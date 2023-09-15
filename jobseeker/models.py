from django.db import models
from employers.models import Jobs

# Create your models here.
class ApplicationForm(models.Model):
    job_id = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    qulification = models.TextField()
    resume = models.FileField()
    status = models.BooleanField()

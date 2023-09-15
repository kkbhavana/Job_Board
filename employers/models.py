from django.db import models


# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=250)
    company = models.CharField(max_length=300)
    description = models.TextField()
    skills = models.CharField(max_length=400)
    places = models.CharField(max_length=250)
    salary = models.CharField(max_length=200)

    def __str__(self):
        return self.title

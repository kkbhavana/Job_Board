from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

class User(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_jobseeker = models.BooleanField(default=False)

    def __str__(self):
        return self.username

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)





class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    about = models.TextField()
    company_name = models.CharField(max_length=300,null=True,blank=True)
    location = models.CharField(max_length=300,null=True,blank=True)
    current_job = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.company_name


class Qulification(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Specialization(models.Model):
    special_title = models.CharField(max_length=200)

    def __str__(self):
        return self.special_title


class Jobseeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    qulification = models.ForeignKey(Qulification, on_delete=models.CASCADE, related_name='education',null=True)
    date_of_passout = models.DateField(null=True)
    specializations = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='course_list',
                                        null=True)
    resume = models.FileField()
    about = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.about

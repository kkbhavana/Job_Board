from django.contrib import admin

from .models import Jobs, ApplicationForm

# Register your models here.
admin.site.register(Jobs),
admin.site.register(ApplicationForm)


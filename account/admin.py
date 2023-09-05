from django.contrib import admin

from .models import User, Employer, Qulification, Jobseeker,Specialization

# Register your models here.
admin.site.register(User),
admin.site.register(Employer),
admin.site.register(Qulification),
admin.site.register(Specialization),
admin.site.register(Jobseeker),


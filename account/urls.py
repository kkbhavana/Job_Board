from django.urls import path

from .views import EmployerRegisterView, JoobseekerRegisterView, CustomAuthToken, EmployerOnlyView, JobseekerOnlyView, \
    LogoutView

urlpatterns=[
    path('emplyoer_register/',EmployerRegisterView.as_view(),name='emp_register'),
    path('jobseeker_register/',JoobseekerRegisterView.as_view(),name='job_register'),
    path('login/',CustomAuthToken.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('employer-verify/',EmployerOnlyView.as_view(),name='emp_verify'),
    path('jobseeker-verify/',JobseekerOnlyView.as_view(),name='job_verify')
]
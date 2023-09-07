from django.urls import path

from .views import EmployerRegisterView, JoobseekerRegisterView, CustomAuthToken, EmployerOnlyView, JobseekerOnlyView, \
    LogoutView, EmployerProfileView, EmployerProfileUpdateView, JobseekerProfileView, JobseekerProfileUpdateView

urlpatterns = [
    path('employer_register/', EmployerRegisterView.as_view(), name='emp_register'),
    path('jobseeker_register/', JoobseekerRegisterView.as_view(), name='job_register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('employer-verify/', EmployerOnlyView.as_view(), name='emp_verify'),
    path('jobseeker-verify/', JobseekerOnlyView.as_view(), name='job_verify'),
    path('employer-profile/', EmployerProfileView.as_view(), name='emp_profile'),
    path('emp-profile-update/<int:pk>/', EmployerProfileUpdateView.as_view(), name='emp_update'),
    path('jobseeker-profile/', JobseekerProfileView.as_view(), name='job_profile'),
    path('job-profile-update/<int:pk>/', JobseekerProfileUpdateView.as_view(), name='jon_update'),

]

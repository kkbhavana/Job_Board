from django.urls import path

from .views import JobDetailView, SeekerJobListView, ApplicationListCreateView, SearchJobView, JobseekerProfileView, \
    JobseekerProfileUpdateView

urlpatterns = [

    path('detail-job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('seeker-list/', SeekerJobListView.as_view(), name='job_list'),
    path('list_create-application/', ApplicationListCreateView.as_view(), name='application'),
    path('search-job/', SearchJobView.as_view(), name='search'),
    path('jobseeker-profile/', JobseekerProfileView.as_view(), name='job_profile'),
    path('job-profile-update/<int:pk>/', JobseekerProfileUpdateView.as_view(), name='jon_update'),

]

from django.urls import path

from .views import JobListCreateView, JobUpdateView, JobDeleteView, JobDetailView, SeekerJobListView, \
    ApplicationListCreateView, SearchJobView

urlpatterns = [
    path('list_create-job/',JobListCreateView.as_view(),name='job_create'),
    path('update-job/<int:pk>/',JobUpdateView.as_view(),name='job_update'),
    path('delete-job/<int:pk>/',JobDeleteView.as_view(),name='job_delete'),
    path('detail-job/<int:pk>/',JobDetailView.as_view(),name='job_detail'),
    path('seeker-list/',SeekerJobListView.as_view(),name='job_list'),
    path('list_create-application/',ApplicationListCreateView.as_view(),name='application'),
    path('search-job/',SearchJobView.as_view(),name='search'),


]
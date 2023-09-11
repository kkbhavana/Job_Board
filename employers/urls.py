from django.urls import path

from .views import JobListCreateView, JobUpdateView, JobDeleteView

urlpatterns = [
    path('list_create-job/', JobListCreateView.as_view(), name='job_create'),
    path('update-job/<int:pk>/', JobUpdateView.as_view(), name='job_update'),
    path('delete-job/<int:pk>/', JobDeleteView.as_view(), name='job_delete'),

]

from django.shortcuts import render
from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response

from account.permission import IsJobseeker
from employers.serializer import JobSerializer

from employers.models import Jobs
from jobseeker.models import ApplicationForm
from jobseeker.serializer import ApplicationFormSerializer
from account.serializers import JobseekerSerializer
from account.models import Jobseeker

# Create your views here.
class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsJobseeker]
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = JobSerializer(queryset, many=False)
        return Response(serializer.data)


class SeekerJobListView(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsJobseeker]
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()


class ApplicationListCreateView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsJobseeker]
    serializer_class = ApplicationFormSerializer
    queryset = ApplicationForm.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ApplicationFormSerializer(queryset, many=True)
        return Response(serializer.data)


class SearchJobView(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsJobseeker]
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'places']


class JobseekerProfileView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsJobseeker]
    serializer_class = JobseekerSerializer
    queryset = Jobseeker.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = JobseekerSerializer(queryset, many=True)
        return Response(serializer.data)


class JobseekerProfileUpdateView(generics.UpdateAPIView):
    serializer_class = JobseekerSerializer
    queryset = Jobseeker.objects.all()

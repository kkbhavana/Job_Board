from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.response import Response

from .models import Jobs, ApplicationForm
from .serializer import JobSerializer, ApplicationFormSerializer


# Create your views here.


# Employer Section:

class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data)


class JobUpdateView(generics.UpdateAPIView):
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()


class JobDeleteView(generics.DestroyAPIView):
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()


# Job seeker section

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = JobSerializer(queryset, many=False)
        return Response(serializer.data)

class SeekerJobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()


class ApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicationFormSerializer
    queryset = ApplicationForm.objects.all()

    def list(self, request):
        queryset= self.get_queryset()
        serializer = ApplicationFormSerializer(queryset,many=True)
        return Response(serializer.data)


class SearchJobView(generics.ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','places']

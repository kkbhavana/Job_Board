from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Jobs
from .serializer import JobSerializer


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

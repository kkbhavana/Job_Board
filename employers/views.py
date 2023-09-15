from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Jobs
from .serializer import JobSerializer
from account.permission import IsEmployer
from account.serializers import EmployerSerializer
from account.models import Employer
# Create your views here.
class JobListCreateView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsEmployer]
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data)


class JobUpdateView(generics.UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsEmployer]
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()


class JobDeleteView(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsEmployer]
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()


class EmployerProfileView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsEmployer]
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EmployerSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployerProfileUpdateView(generics.RetrieveUpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated & IsEmployer]
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()

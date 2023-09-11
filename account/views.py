from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employer
from .permission import IsEmployer, IsJobseeker
from .serializers import EmpoloyerRegisterSerializer, UserSerializer, JobseekerRegisterSerializer, EmployerSerializer, \
    Jobseeker, JobseekerSerializer


# Create your views here.

class EmployerRegisterView(generics.GenericAPIView):
    serializer_class = EmpoloyerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
        })


class JoobseekerRegisterView(generics.GenericAPIView):
    serializer_class = JobseekerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
        })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'is_employer': user.is_employer
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class EmployerOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsEmployer]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class JobseekerOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsJobseeker]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user









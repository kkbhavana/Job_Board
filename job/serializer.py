from rest_framework import serializers

from .models import Jobs, ApplicationForm


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"

class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model= ApplicationForm
        fields = '__all__'
from rest_framework import serializers
from .models import User, Employer, Jobseeker


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_employer',)


class EmpoloyerRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password2 != password:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password)
        user.is_employer = True
        user.save()
        Employer.objects.create(user=user)
        return user


class JobseekerRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password2 != password:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password)
        user.is_jobseeker = True
        user.save()
        Jobseeker.objects.create(user=user)
        return user


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class JobseekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobseeker
        fields = '__all__'

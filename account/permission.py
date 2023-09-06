from rest_framework.permissions import BasePermission


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_employer)


class IsJobseeker(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_jobseeker)
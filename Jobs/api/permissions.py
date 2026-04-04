from django.contrib.auth.models import User
from rest_framework import permissions

class PostJobs(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.is_authenticated and request.user.type == "employer") or (request.user.is_authenticated and request.user.is_staff)
    
class EditJobs(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and (obj.posted_by == request.user or request.user.is_staff)
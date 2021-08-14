from rest_framework import permissions
from rest_framework.request import Request

from ..models import Review


class IsAdminOrReadonly(permissions.IsAdminUser):
    def has_permission(self, request: Request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        admin_permission = bool(request.user and request.user.is_staff)
        return admin_permission


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj: Review):
        print(request.user)
        if request.method in permissions.SAFE_METHODS:
            return True
        is_author = request.user.id == obj.author.id
        return is_author

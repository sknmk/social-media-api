from rest_framework import permissions


class IsAdminOrIsSelfOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if bool(request.method in permissions.SAFE_METHODS or request.user and request.user.is_staff):
            return True
        if hasattr(obj, 'user'):
            return request.user == obj.user
        if hasattr(obj, 'author'):
            return request.user == obj.author

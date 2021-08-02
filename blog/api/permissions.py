from rest_framework import permissions


class IsAdminOrIsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if bool(request.method in permissions.SAFE_METHODS or request.user and request.user.is_staff):
            return True
        return request.user == obj.author

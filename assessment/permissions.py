from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow only admin users to perform POST, PUT, and DELETE requests
        return request.user.is_staff


class IsAdminOrCandidate(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "retrieve":
            return request.user.is_authenticated
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        # Allow candidates to read their own assessment results
        if view.action == "retrieve":
            return obj.candidate == request.user or request.user.is_staff
        return request.method in permissions.SAFE_METHODS

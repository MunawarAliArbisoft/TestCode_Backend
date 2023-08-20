from rest_framework import permissions


class CandidatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["retrieve", "update", "partial_update"]:
            return request.user.is_authenticated
        elif view.action == "destroy":
            return request.user.is_staff
        if view.action == "list":
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == "create":
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "partial_update", "retrieve"]:
            return obj == request.user or request.user.is_staff
        elif view.action == "destroy":
            return request.user.is_staff
        else:
            return False

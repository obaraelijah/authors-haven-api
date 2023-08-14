from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    safe methods -> get, head , options (because they do not modify objs state)
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user

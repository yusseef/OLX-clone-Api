from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return obj.owner.id == request.user.id
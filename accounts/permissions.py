from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        else:
            if request.user.is_authenticated and request.user.is_staff == True:

                return True

            else:

                raise PermissionDenied(detail={'message': 'Permission denied. User is not an admin'})

class IsAdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_staff == True:

            return True

        else:

            raise PermissionDenied(detail={'message': 'Permission denied. User is not an admin'})
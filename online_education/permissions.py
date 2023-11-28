from rest_framework.permissions import BasePermission


class IsOwnerOrManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderators'):
            return True

        return request.user == view.get_object().owner

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
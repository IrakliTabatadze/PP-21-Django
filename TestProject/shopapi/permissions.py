from rest_framework.permissions import BasePermission


class SimplePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.has_perm('shop.add_product')

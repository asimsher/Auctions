from rest_framework import permissions


class UserEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class CheckUserSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'seller'


class CheckUserBuyer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'buyer'


class CheckCarEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.seller == request.user


class CheckAuctionEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.car.seller == request.user
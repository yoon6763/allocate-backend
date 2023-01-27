from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS 는 데이터에 영향을 주지 않는 메소드 (GET 등)을 의미
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

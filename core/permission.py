from rest_framework import permissions

class AdminOrReadonly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS) or bool(request.user and request.user.is_staff)
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user == obj.review_user) or bool(request.user and request.user.is_staff)
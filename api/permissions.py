from rest_framework import permissions

class MyPermissions(permissions.BasePermission):        

    def has_permission(self, request, view):
        if request.method == 'GET' and request.user.is_authenticated:
            return True
        elif request.user.is_staff:
            return True
        else:
            return False
        

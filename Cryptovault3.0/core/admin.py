from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view this admin site.
        """
        print(f"--- CUSTOM ADMIN PERMISSION CHECK for user: {request.user.email} ---")
        print(f"  Is Active: {request.user.is_active}")
        print(f"  Is Staff: {request.user.is_staff}")
        print(f"  Is Superuser: {request.user.is_superuser}")
        
        # Superusers should always have permission
        if request.user.is_superuser:
            print("  User is a superuser, granting access.")
            return True
            
        # Standard staff check
        permission = request.user.is_active and request.user.is_staff
        print(f"  Final permission: {permission}")
        return permission

admin_site = MyAdminSite(name='myadmin') 
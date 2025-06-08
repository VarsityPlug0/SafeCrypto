from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    pass

admin_site = MyAdminSite(name='myadmin') 
from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (
    CustomUser, InvestmentTier, Investment, Deposit, Withdrawal,
    Wallet, Referral, IPAddress, ReferralReward, DailySpecial,
    Backup, AdminActivityLog
)

class MyAdminSite(AdminSite):
    pass

admin_site = MyAdminSite(name='myadmin')

# A simple ModelAdmin to display the models
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'level', 'is_staff', 'is_superuser')

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'tier', 'amount', 'is_active', 'end_date')

class DepositAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'created_at')

class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'created_at')

# Register models with the custom admin site
admin_site.register(CustomUser, CustomUserAdmin)
admin_site.register(InvestmentTier)
admin_site.register(Investment, InvestmentAdmin)
admin_site.register(Deposit, DepositAdmin)
admin_site.register(Withdrawal, WithdrawalAdmin)
admin_site.register(Wallet)
admin_site.register(Referral)
admin_site.register(IPAddress)
admin_site.register(ReferralReward)
admin_site.register(DailySpecial)
admin_site.register(Backup)
admin_site.register(AdminActivityLog) 
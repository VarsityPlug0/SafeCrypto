from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (
    CustomUser, InvestmentTier, Investment, Deposit, Withdrawal,
    Wallet, Referral, IPAddress, ReferralReward, DailySpecial,
    Backup, AdminActivityLog
)
from django.utils.html import format_html

class MyAdminSite(AdminSite):
    pass

admin_site = MyAdminSite(name='myadmin')

# A simple ModelAdmin to display the models
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'level', 'is_staff', 'is_superuser')

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'tier', 'amount', 'is_active', 'end_date')

class DepositAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'created_at', 'display_proof')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email')
    actions = ['approve_deposits']
    
    def display_proof(self, obj):
        if obj.proof_image:
            return format_html('<a href="{}" target="_blank">View Proof</a>', obj.proof_image.url)
        return "No proof"
    display_proof.short_description = "Proof of Payment"

    def approve_deposits(self, request, queryset):
        for deposit in queryset:
            if deposit.status == 'pending':
                deposit.status = 'approved'
                deposit.save()
        self.message_user(request, f"{queryset.count()} deposits were successfully approved.")
    approve_deposits.short_description = "Approve selected deposits"

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
from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import (
    CustomUser, InvestmentTier, Investment, Deposit, Withdrawal,
    Wallet, Referral, IPAddress, ReferralReward, DailySpecial,
    Backup, AdminActivityLog, Voucher
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

class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

class VoucherAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'created_at', 'display_voucher')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email')
    actions = ['approve_vouchers', 'reject_vouchers']

    def display_voucher(self, obj):
        if obj.voucher_image:
            return format_html('<a href="{}" target="_blank">View Voucher</a>', obj.voucher_image.url)
        return "No voucher"
    display_voucher.short_description = "Voucher Image"

    def approve_vouchers(self, request, queryset):
        for voucher in queryset:
            if voucher.status == 'pending':
                voucher.status = 'approved'
                voucher.save()
        self.message_user(request, f"{queryset.count()} vouchers were successfully approved.")
    approve_vouchers.short_description = "Approve selected vouchers"

    def reject_vouchers(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, f"{queryset.count()} vouchers were rejected.")
    reject_vouchers.short_description = "Reject selected vouchers"

# Register models with the custom admin site
admin_site.register(CustomUser, CustomUserAdmin)
admin_site.register(InvestmentTier)
admin_site.register(Investment, InvestmentAdmin)
admin_site.register(Deposit, DepositAdmin)
admin_site.register(Withdrawal, WithdrawalAdmin)
admin_site.register(Wallet, WalletAdmin)
admin_site.register(Referral)
admin_site.register(IPAddress)
admin_site.register(ReferralReward)
admin_site.register(DailySpecial)
admin_site.register(Backup)
admin_site.register(AdminActivityLog)
admin_site.register(Voucher, VoucherAdmin) 
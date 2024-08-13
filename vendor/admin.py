from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("vendor_name", "user", "created_at", "is_approved")
    list_display_links = ("vendor_name", "user")
    list_editable = ('is_approved',)
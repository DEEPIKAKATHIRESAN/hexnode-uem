from django.contrib import admin
from .models import Device, Policy, DeviceGroup

admin.site.site_header = 'Hexnode UEM Admin'
admin.site.site_title  = 'UEM Admin'
admin.site.index_title = 'Endpoint Management'


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display   = ['name', 'serial_number', 'os_type', 'status', 'owner_name', 'group', 'enrolled_at']
    list_filter    = ['os_type', 'status', 'group']
    search_fields  = ['name', 'serial_number', 'owner_name', 'owner_email']
    list_editable  = ['status']


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display  = ['name', 'policy_type', 'is_active', 'created_at']
    list_filter   = ['policy_type', 'is_active']


@admin.register(DeviceGroup)
class DeviceGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']

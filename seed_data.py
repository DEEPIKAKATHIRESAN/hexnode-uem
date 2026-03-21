"""
Run this after migrations to load demo data:
    python manage.py shell < seed_data.py
"""
import os, sys, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uem_project.settings')
django.setup()

from uem_app.models import Device, Policy, DeviceGroup

# Groups
sales, _    = DeviceGroup.objects.get_or_create(name='Sales Team',    defaults={'description': 'Field sales devices'})
engineering, _ = DeviceGroup.objects.get_or_create(name='Engineering', defaults={'description': 'Developer laptops'})
hr, _       = DeviceGroup.objects.get_or_create(name='HR & Finance',  defaults={'description': 'HR department devices'})

# Policies
p1, _ = Policy.objects.get_or_create(name='Passcode Policy',   defaults={'policy_type': 'passcode',     'description': 'Require 6-digit PIN', 'is_active': True})
p2, _ = Policy.objects.get_or_create(name='Office Wi-Fi',      defaults={'policy_type': 'wifi',         'description': 'Push office Wi-Fi config', 'is_active': True})
p3, _ = Policy.objects.get_or_create(name='VPN Config',        defaults={'policy_type': 'vpn',          'description': 'Corporate VPN profile', 'is_active': True})
p4, _ = Policy.objects.get_or_create(name='App Restrictions',  defaults={'policy_type': 'restrictions', 'description': 'Block social media apps', 'is_active': False})

# Devices
devices = [
    {'name': 'John iPhone 14',    'serial_number': 'SN-IOS-001',  'os_type': 'ios',     'os_version': '17.2', 'model': 'iPhone 14 Pro',      'owner_name': 'John Smith',   'owner_email': 'john@company.com',   'status': 'active',   'group': sales,       'policy': p1},
    {'name': 'Mary Samsung S23',  'serial_number': 'SN-AND-002',  'os_type': 'android', 'os_version': '14',   'model': 'Samsung Galaxy S23',  'owner_name': 'Mary Johnson', 'owner_email': 'mary@company.com',   'status': 'active',   'group': sales,       'policy': p1},
    {'name': 'Dev MacBook Pro',   'serial_number': 'SN-MAC-003',  'os_type': 'macos',   'os_version': '14.1', 'model': 'MacBook Pro 14"',     'owner_name': 'Ravi Kumar',   'owner_email': 'ravi@company.com',   'status': 'active',   'group': engineering, 'policy': p2},
    {'name': 'Dev Windows PC',    'serial_number': 'SN-WIN-004',  'os_type': 'windows', 'os_version': '11',   'model': 'Dell XPS 15',         'owner_name': 'Priya Nair',   'owner_email': 'priya@company.com',  'status': 'active',   'group': engineering, 'policy': p3},
    {'name': 'HR Laptop',         'serial_number': 'SN-WIN-005',  'os_type': 'windows', 'os_version': '10',   'model': 'HP EliteBook 840',    'owner_name': 'Anita Das',    'owner_email': 'anita@company.com',  'status': 'inactive', 'group': hr,          'policy': p4},
    {'name': 'Lost Field Phone',  'serial_number': 'SN-AND-006',  'os_type': 'android', 'os_version': '13',   'model': 'OnePlus 11',          'owner_name': 'Tom Wilson',   'owner_email': 'tom@company.com',    'status': 'lost',     'group': sales,       'policy': p1},
    {'name': 'Linux Dev Box',     'serial_number': 'SN-LNX-007',  'os_type': 'linux',   'os_version': 'Ubuntu 22.04', 'model': 'ThinkPad X1', 'owner_name': 'Arjun Menon', 'owner_email': 'arjun@company.com',  'status': 'active',   'group': engineering, 'policy': p3},
    {'name': 'iPad Air HR',       'serial_number': 'SN-IOS-008',  'os_type': 'ios',     'os_version': '17.0', 'model': 'iPad Air 5',          'owner_name': 'Sneha Pillai', 'owner_email': 'sneha@company.com',  'status': 'active',   'group': hr,          'policy': p2},
]

for d in devices:
    Device.objects.get_or_create(serial_number=d['serial_number'], defaults=d)

print("✅  Demo data loaded!")
print(f"   Groups:   {DeviceGroup.objects.count()}")
print(f"   Policies: {Policy.objects.count()}")
print(f"   Devices:  {Device.objects.count()}")

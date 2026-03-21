from django import forms
from .models import Device, Policy, DeviceGroup

W = {'class': 'form-control'}
S = {'class': 'form-select'}


class DeviceForm(forms.ModelForm):
    class Meta:
        model  = Device
        fields = ['name', 'serial_number', 'os_type', 'os_version',
                  'model', 'owner_name', 'owner_email', 'status', 'group', 'policy']
        widgets = {
            'name':          forms.TextInput(attrs={**W, 'placeholder': 'e.g. John iPhone 14'}),
            'serial_number': forms.TextInput(attrs={**W, 'placeholder': 'e.g. SN123456789'}),
            'os_type':       forms.Select(attrs=S),
            'os_version':    forms.TextInput(attrs={**W, 'placeholder': 'e.g. 16.5'}),
            'model':         forms.TextInput(attrs={**W, 'placeholder': 'e.g. iPhone 14 Pro'}),
            'owner_name':    forms.TextInput(attrs={**W, 'placeholder': 'Employee name'}),
            'owner_email':   forms.EmailInput(attrs={**W, 'placeholder': 'employee@company.com'}),
            'status':        forms.Select(attrs=S),
            'group':         forms.Select(attrs=S),
            'policy':        forms.Select(attrs=S),
        }


class PolicyForm(forms.ModelForm):
    class Meta:
        model  = Policy
        fields = ['name', 'policy_type', 'description', 'is_active']
        widgets = {
            'name':        forms.TextInput(attrs={**W, 'placeholder': 'Policy name'}),
            'policy_type': forms.Select(attrs=S),
            'description': forms.Textarea(attrs={**W, 'rows': 3}),
            'is_active':   forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model  = DeviceGroup
        fields = ['name', 'description']
        widgets = {
            'name':        forms.TextInput(attrs={**W, 'placeholder': 'e.g. Sales Team'}),
            'description': forms.Textarea(attrs={**W, 'rows': 2}),
        }

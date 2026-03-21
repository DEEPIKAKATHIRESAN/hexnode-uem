from django.db import models
from django.utils import timezone


class DeviceGroup(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Policy(models.Model):
    TYPE_CHOICES = [
        ('passcode',     'Passcode'),
        ('wifi',         'Wi-Fi'),
        ('vpn',          'VPN'),
        ('restrictions', 'Restrictions'),
        ('app',          'App Management'),
    ]
    name        = models.CharField(max_length=100)
    policy_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    description = models.TextField(blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering     = ['-created_at']
        verbose_name_plural = 'Policies'


class Device(models.Model):
    OS_CHOICES = [
        ('android', 'Android'),
        ('ios',     'iOS'),
        ('windows', 'Windows'),
        ('macos',   'macOS'),
        ('linux',   'Linux'),
    ]
    STATUS_CHOICES = [
        ('active',   'Active'),
        ('inactive', 'Inactive'),
        ('lost',     'Lost'),
        ('wiped',    'Wiped'),
    ]

    name          = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=100, unique=True)
    os_type       = models.CharField(max_length=20, choices=OS_CHOICES)
    os_version    = models.CharField(max_length=50, blank=True)
    model         = models.CharField(max_length=100, blank=True)
    owner_name    = models.CharField(max_length=150, blank=True)
    owner_email   = models.EmailField(blank=True)
    status        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    group         = models.ForeignKey(DeviceGroup, on_delete=models.SET_NULL, null=True, blank=True, related_name='devices')
    policy        = models.ForeignKey(Policy,      on_delete=models.SET_NULL, null=True, blank=True, related_name='devices')
    enrolled_at   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

    class Meta:
        ordering = ['-enrolled_at']

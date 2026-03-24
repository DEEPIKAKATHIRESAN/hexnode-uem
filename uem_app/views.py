from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Device, Policy, DeviceGroup
from .forms import DeviceForm, PolicyForm, GroupForm


@login_required
def dashboard(request):
    context = {
        'total_devices':   Device.objects.count(),
        'active_devices':  Device.objects.filter(status='active').count(),
        'lost_devices':    Device.objects.filter(status='lost').count(),
        'total_policies':  Policy.objects.count(),
        'total_groups':    DeviceGroup.objects.count(),
        'recent_devices':  Device.objects.select_related('group', 'policy')[:6],
        'os_stats':        Device.objects.values('os_type').annotate(count=Count('id')),
    }
    return render(request, 'uem/dashboard.html', context)


# ── Devices ──────────────────────────────────────────────────────────────────

@login_required
def device_list(request):
    qs = Device.objects.select_related('group', 'policy')
    q  = request.GET.get('q', '')
    st = request.GET.get('status', '')
    os = request.GET.get('os', '')
    if q:
        qs = qs.filter(name__icontains=q) | qs.filter(serial_number__icontains=q) | qs.filter(owner_name__icontains=q)
    if st:
        qs = qs.filter(status=st)
    if os:
        qs = qs.filter(os_type=os)
    return render(request, 'uem/device_list.html', {'devices': qs, 'q': q, 'status': st, 'os': os})


@login_required
def device_add(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        d = form.save()
        messages.success(request, f'Device "{d.name}" enrolled successfully!')
        return redirect('device_list')
    return render(request, 'uem/form.html', {'form': form, 'title': 'Enroll New Device', 'back': 'device_list'})


@login_required
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, 'uem/device_detail.html', {'device': device})


@login_required
def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == 'POST':
        messages.success(request, f'Device "{device.name}" removed.')
        device.delete()
        return redirect('device_list')
    return render(request, 'uem/confirm_delete.html', {'obj': device, 'back': 'device_list'})


# ── Policies ─────────────────────────────────────────────────────────────────

@login_required
def policy_list(request):
    policies = Policy.objects.annotate(device_count=Count('devices'))
    return render(request, 'uem/policy_list.html', {'policies': policies})


@login_required
def policy_add(request):
    form = PolicyForm(request.POST or None)
    if form.is_valid():
        p = form.save()
        messages.success(request, f'Policy "{p.name}" created!')
        return redirect('policy_list')
    return render(request, 'uem/form.html', {'form': form, 'title': 'Create Policy', 'back': 'policy_list'})


@login_required
def policy_delete(request, pk):
    policy = get_object_or_404(Policy, pk=pk)
    if request.method == 'POST':
        messages.success(request, f'Policy "{policy.name}" deleted.')
        policy.delete()
        return redirect('policy_list')
    return render(request, 'uem/confirm_delete.html', {'obj': policy, 'back': 'policy_list'})


# ── Groups ────────────────────────────────────────────────────────────────────

@login_required
def group_list(request):
    groups = DeviceGroup.objects.annotate(device_count=Count('devices'))
    return render(request, 'uem/group_list.html', {'groups': groups})


@login_required
def group_add(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        g = form.save()
        messages.success(request, f'Group "{g.name}" created!')
        return redirect('group_list')
    return render(request, 'uem/form.html', {'form': form, 'title': 'Create Group', 'back': 'group_list'})


@login_required
def filevault(request):
    devices   = Device.objects.filter(os_type__in=['macos', 'windows', 'linux', 'android', 'ios'])
    device_id = request.GET.get('device')
    selected  = Device.objects.filter(pk=device_id).first() if device_id else None
    return render(request, 'uem/filevault.html', {'devices': devices, 'selected': selected})


@login_required
def remote_access(request):
    devices  = Device.objects.all()
    device_id = request.GET.get('device')
    selected = None
    if device_id:
        selected = Device.objects.filter(pk=device_id).first()
    return render(request, 'uem/remote_access.html', {
        'devices': devices,
        'selected': selected,
    })


@login_required
def group_delete(request, pk):
    group = get_object_or_404(DeviceGroup, pk=pk)
    if request.method == 'POST':
        messages.success(request, f'Group "{group.name}" deleted.')
        group.delete()
        return redirect('group_list')
    return render(request, 'uem/confirm_delete.html', {'obj': group, 'back': 'group_list'})

# Hexnode UEM — Mini Django Project

A simplified Unified Endpoint Management (UEM) system built with Django.
Great for interview demos!

---

## Features

- Login / Logout with Django Auth
- Dashboard with live stats and OS breakdown
- Device Management — enroll, view, filter, delete
- Policy Management — passcode, Wi-Fi, VPN, restrictions
- Device Groups — organise devices by team
- Remote Actions UI — Lock, Wipe, Locate, Sync
- Django Admin Panel at `/admin/`
- Filter & Search on device list

---

## Setup (Run These Commands)

### Step 1 — Install Django
```bash
pip install -r requirements.txt
```

### Step 2 — Run Migrations
```bash
python manage.py makemigrations uem_app
python manage.py migrate
```

### Step 3 — Create Admin User
```bash
python manage.py createsuperuser
```
Enter a username and password when prompted.

### Step 4 — Load Demo Data (optional but recommended)
```bash
python manage.py shell < seed_data.py
```

### Step 5 — Start the Server
```bash
python manage.py runserver
```

Open your browser and go to: **http://127.0.0.1:8000**

---

## Project Structure

```
hexnode_uem/
├── manage.py
├── requirements.txt
├── seed_data.py          ← loads demo devices/policies/groups
├── uem_project/
│   ├── settings.py
│   └── urls.py
├── uem_app/
│   ├── models.py         ← Device, Policy, DeviceGroup
│   ├── views.py          ← All CRUD logic
│   ├── forms.py          ← Django forms
│   └── admin.py          ← Admin config
└── templates/
    ├── registration/
    │   └── login.html
    └── uem/
        ├── base.html         ← Sidebar layout
        ├── dashboard.html
        ├── device_list.html
        ├── device_detail.html
        ├── policy_list.html
        ├── group_list.html
        ├── form.html         ← Reusable add form
        └── confirm_delete.html
```

---

## Pages / URLs

| URL | Page |
|-----|------|
| `/` | Dashboard |
| `/devices/` | Device list with search & filter |
| `/devices/add/` | Enroll new device |
| `/devices/<id>/` | Device detail + remote actions |
| `/policies/` | Policy list |
| `/policies/add/` | Create policy |
| `/groups/` | Group list |
| `/groups/add/` | Create group |
| `/admin/` | Django admin |
| `/login/` | Login page |

user_name='domownik'
manager_name = 'zarzadca'

user_perms = [
   'can_view_event',
   'can_view_login_attempt',
]

manager_perms = [
   'can_view_event',
   'can_view_login_attempt',
   'add_keyboard',
   'add_sensor',
   'change_keyboard',
   'change_sensor',
   'delete_keyboard',
   'delete_sensor',
]

def createGroupAndUpdatePermissions(group_name, group_perms):
    try:
        group = Group.objects.get(name = group_name)
    except Group.DoesNotExist:
        group = Group(name = group_name)
        group.save()

    for perm_codename in group_perms:
        try:
            perm = Permission.objects.get(codename = perm_codename)
            group.permissions.add(perm)
        except Permission.DoesNotExist:
            if __name__ == "__main__":
                print "Permission %s does not exist. Passing." % perm_codename

    group.save()

if __name__ == "__main__":
    import imp
    import os, sys

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projektinzynierski.settings")
    try:
        imp.find_module('projektinzynierski/settings') # Assumed to be in the same directory.
    except ImportError:
        sys.stderr.write("Error: Can't find the file 'settings.py' in the\
                          directory containing %r. It appears you've customized\
                          things.\nYou'll have to run django-admin.py, passing\
                          it your settings module.\n" % __file__)
        sys.exit(1)

    from django.contrib.auth.models import Group, Permission

    createGroupAndUpdatePermissions(user_name, user_perms)
    createGroupAndUpdatePermissions(manager_name, manager_perms)

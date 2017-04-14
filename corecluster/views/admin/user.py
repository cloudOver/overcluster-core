"""
Copyright (C) 2014-2017 cloudover.io ltd.
This file is part of the CloudOver.org project

Licensee holding a valid commercial license for this software may
use it in accordance with the terms of the license agreement
between cloudover.io ltd. and the licensee.

Alternatively you may use this software under following terms of
GNU Affero GPL v3 license:

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version. For details contact
with the cloudover.io company: https://cloudover.io/


This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.


You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from django.contrib import admin
from corecluster.views.admin_site import admin_site
from corecluster.models.core.user import User


class UserAdmin(admin.ModelAdmin):
    actions = ['delete_selected', 'deactivate', 'activate']
    readonly_fields = ['id', 'last_task', 'state']
    list_display = ['login', 'name', 'surname', 'email', 'state', 'registration_date', 'total_vms', 'defined_vms', 'running_vms']

    list_filter = ('state', 'group')
    ordering = ('login',)

    def has_add_permission(self, request):
        return False


    def save_model(self, request, obj, form, change):
        obj.set_state(obj.default_state)
        obj.save()


    def activate(self, request, queryset):
        names = []
        for s in queryset.all():
            s.set_state('ok')
            s.save()

            names.append(s.name)
        self.message_user(request, 'User account(s) %s are active.' % ', '.join(names))
    activate.short_description = 'Activate account'


    def remove(self, request, queryset):
        names = []
        for s in queryset.all():
            s.set_state('removed')
            s.save()

            names.append(s.name)
        self.message_user(request, 'User account(s) %s are removed.' % ', '.join(names))
    remove.short_description = 'Remove account'


    def deactivate(self, request, queryset):
        names = []
        for s in queryset.all():
            s.set_state('inactive')
            s.save()

            names.append(s.name)
        self.message_user(request, 'User account(s) %s are inactive.' % ', '.join(names))
    deactivate.short_description = 'Lock account'


admin_site.register(User, UserAdmin)

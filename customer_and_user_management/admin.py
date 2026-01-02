from django.contrib import admin
from django import forms

from .models import (
    User, Permission, Country, Customer, Group,
    GroupRole, RolePermission, UserRole, Role, UserGroup
)


# Permission
class PermissionAdminForm(forms.ModelForm):
    """Custom admin form for managing Permission objects."""

    class Meta:
        model = Permission
        fields = '__all__'

    def clean(self):
        """Custom admin form for managing Permission objects."""
        cleaned_data = super().clean()
        if not cleaned_data.get('permission'):
            raise forms.ValidationError('Permission name is required.')
        if cleaned_data.get('status') not in [True, False]:
            raise forms.ValidationError(
                'Invalid status value. Status must be either True or False.')


class PermissionAdmin(admin.ModelAdmin):
    """Custom admin form for managing Permission objects."""

    form = PermissionAdminForm


admin.site.register(Permission, PermissionAdmin)


# Country
class CountryForm(forms.ModelForm):
    """Custom admin form for managing Country objects."""

    class Meta:
        model = Country
        fields = '__all__'


class CountryAdmin(admin.ModelAdmin):
    """Custom admin form for managing CountryForm objects."""

    form = CountryForm


admin.site.register(Country, CountryAdmin)


# User
class UserForm(forms.ModelForm):
    """Custom admin form for managing User objects."""

    class Meta:
        model = User
        fields = '__all__'


class UserAdmin(admin.ModelAdmin):
    """Admin model for User."""

    form = UserForm


admin.site.register(User, UserAdmin)


# Customer
class CustomerForm(forms.ModelForm):
    """Custom admin form for managing Customer objects."""

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    """Admin model for Customer."""

    form = CustomerForm


admin.site.register(Customer, CustomerAdmin)


# Group
class GroupForm(forms.ModelForm):
    """Custom admin form for managing Group objects."""

    class Meta:
        model = Group
        fields = '__all__'


class GroupAdmin(admin.ModelAdmin):
    """Admin model for Group. """

    form = GroupForm


admin.site.register(Group, GroupAdmin)
admin.site.register(Role)
admin.site.register(GroupRole)
admin.site.register(UserRole)
admin.site.register(RolePermission)


# UserGroup


class UserGroupForm(forms.ModelForm):
    """Custom admin form for managing UserGroup objects."""

    class Meta:
        model = UserGroup
        fields = ['user_group_id', 'user_id', 'group_id',
                  'status', 'is_group_lead']


class UserGroupAdmin(admin.ModelAdmin):
    """Admin model for UserGroup."""

    form = UserGroupForm


admin.site.register(UserGroup, UserGroupAdmin)

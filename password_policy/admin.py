from django.contrib import admin
from .models import PasswordPolicyRule, PasswordPolicy

admin.site.register(PasswordPolicyRule)
admin.site.register(PasswordPolicy)

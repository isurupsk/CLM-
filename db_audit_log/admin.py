from django.contrib import admin

# Register your models here.


from .models import DbAuditLog

# admin.site.register(User)
admin.site.register(DbAuditLog)

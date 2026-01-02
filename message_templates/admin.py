from django.contrib import admin

# Register your models here.
from .models import (
    NotificationEvent, NotificationPerod, EmailTemplate,
    SmsTemplate, NotificationSchedule
)

admin.site.register(NotificationEvent)
admin.site.register(NotificationPerod)
admin.site.register(EmailTemplate)
admin.site.register(SmsTemplate)
admin.site.register(NotificationSchedule)

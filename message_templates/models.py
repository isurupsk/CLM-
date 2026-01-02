from django.db import models
from contract.models import Contract

from customer_and_user_management.models import Customer

# NotificationEvent


class NotificationEvent(models.Model):
    """Model representing an Notification Event."""

    notification_event_id = models.AutoField(primary_key=True)
    notification_event = models.TextField()
    status = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name_plural = "1. NotificationEvent"

# NotificationPerod


class NotificationPerod(models.Model):
    """Model representing an Notification Perod."""

    notification_period_id = models.AutoField(primary_key=True)
    template_type = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    number_of_reminders = models.IntegerField()
    gap_between_reminders = models.IntegerField()
    days_in_advance = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    notification_event = models.ForeignKey(
        NotificationEvent, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "2. NotificationPerod"

# EamilTemplate


class EmailTemplate(models.Model):
    """Model representing an Eamil Template."""

    email_template_id = models.AutoField(primary_key=True)
    template_text = models.TextField()
    notication_event = models.ForeignKey(
        NotificationEvent, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name_plural = "2. EmailTemplate"

# SmsTemplate


class SmsTemplate(models.Model):
    """Model representing an SMS template."""

    sms_template_id = models.AutoField(primary_key=True)
    template_text = models.TextField()
    notication_event = models.ForeignKey(
        NotificationEvent, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name_plural = "3. SmsTemplate"

# NotificationSchedule


class NotificationSchedule(models.Model):
    """Model representing an Notification Schedule."""

    notification_scheudle_id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    schedule_date = models.DateTimeField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

from django.db import models
from django.forms import ValidationError
from contract.models import Contract

from customer_and_user_management.models import Customer, User


# UserActivityLog

class UserActivityLog(models.Model):
    """Model representing the User Activity Log."""

    user_activity_log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=50)
    activity_time = models.DateTimeField(null=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False)
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, null=False)
    activity_type = models.CharField(max_length=20)

    def clean(self):
        """Clean method for the model instance."""

        if not self.activity:
            raise ValidationError('activity   is required.')
        if not self.activity_time:
            raise ValidationError('activity time  is required.')
        if not self. activity_type:
            raise ValidationError(' activity type  is required.')

    class Meta:
        verbose_name_plural = "1. UserActivityLog"

# AnalyticalReportList


class AnalyticalReportList(models.Model):
    """Model representing the Analytical Report List."""

    analytical_report_list_id = models.AutoField(primary_key=True)
    report_name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    status = models.BooleanField(null=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.report_name

    def clean(self):
        """Clean method for the model instance."""
        if not self.report_name:
            raise ValidationError('Report name  is required.')

    class Meta:
        verbose_name_plural = "2. AnalyticalReportList"

# ReportDeliverySchedule


class ReportDeliverySchedule(models.Model):
    """Model representing the Report Delivery Schedule."""

    report_delivery_scheudle_id = models.AutoField(primary_key=True)
    analytical_report_list = models.ForeignKey(
        AnalyticalReportList, on_delete=models.CASCADE, null=False)
    delivery_frequency = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.BooleanField(null=False)
    last_delivered_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    delivery_time = models.DateTimeField()
    start_date = models.DateTimeField(null=False)

    def clean(self):
        """Clean method for the model instance."""
        if not self.delivery_frequency:
            raise ValidationError('Delivery frequency  is required.')
        if not self.start_date:
            raise ValidationError('start date  is required.')

    class Meta:
        verbose_name_plural = "3. ReportDeliverySchedule"

# ReportDeliveryLog


class ReportDeliveryLog(models.Model):
    """Model representing the Report Delivery Log."""

    report_delivery_log_id = models.AutoField(primary_key=True)
    report_delivery_schedule = models.ForeignKey(
        ReportDeliverySchedule, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.BooleanField(null=False)
    error_message = models.CharField(max_length=20)

    def clean(self):
        """Clean method for the model instance."""
        if not self.delivery_date:
            raise ValidationError('delivery_date   is required.')

    class Meta:
        verbose_name_plural = "4. ReportDeliveryLog"

# EmailDeliveryLog


class EmailDeliveryLog(models.Model):
    """Model representing the Email Delivery Log."""

    email_delivery_log_id = models.AutoField(primary_key=True)
    reference_type = models.CharField(max_length=20)
    delivery_date = models.DateTimeField()
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False)
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, null=False)

    def clean(self):
        """Clean method for the model instance."""
        if not self.reference_type:
            raise ValidationError('Reference_type  is required.')

    class Meta:
        verbose_name_plural = "5. EmailDeliveryLog"

# SmsDeliveryLog


class SmsDeliveryLog(models.Model):
    """Model representing the SMS delivery log."""

    sms_delivery_log_id = models.AutoField(primary_key=True)
    reference_type = models.CharField(max_length=20)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False)
    event_or_action = models.CharField(max_length=10)
    sms_body = models.TextField()

    def clean(self):
        if not self.reference_type:
            raise ValidationError('Reference type  is required.')

    class Meta:
        verbose_name_plural = "6. SmsDeliveryLog"

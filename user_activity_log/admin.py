from django import forms
from django.contrib import admin

# Register your models here.

from .models import (
    UserActivityLog, AnalyticalReportList, ReportDeliverySchedule,
    ReportDeliveryLog, EmailDeliveryLog, SmsDeliveryLog
)

# UserActivityLog


class UserActivityLogForm(forms.ModelForm):
    """Form for the UserActivityLog model."""

    class Meta:
        model = UserActivityLog
        fields = '__all__'


class UserActivityLogAdmin(admin.ModelAdmin):
    """Admin configuration for the UserActivityLog model."""

    form = UserActivityLogForm


admin.site.register(UserActivityLog, UserActivityLogAdmin)

# AnalyticalReportList


class AnalyticalReportListForm(forms.ModelForm):
    """Form for the AnalyticalReportList model."""

    class Meta:
        model = AnalyticalReportList
        fields = '__all__'


class AnalyticalReportListAdmin(admin.ModelAdmin):
    """Admin configuration for the AnalyticalReportListForm model."""

    form = AnalyticalReportListForm


admin.site.register(AnalyticalReportList, AnalyticalReportListAdmin)

# ReportDeliverySchedule


class ReportDeliveryScheduleForm(forms.ModelForm):
    """Form for the ReportDeliverySchedule model."""

    class Meta:
        model = ReportDeliverySchedule
        fields = '__all__'


class ReportDeliveryScheduleAdmin(admin.ModelAdmin):
    """Admin configuration for the ReportDeliverySchedule model."""

    form = ReportDeliveryScheduleForm


admin.site.register(ReportDeliverySchedule, ReportDeliveryScheduleAdmin)

# ReportDeliveryLog


class ReportDeliveryLogForm(forms.ModelForm):
    """Form for the ReportDeliveryLog model."""

    class Meta:
        model = ReportDeliveryLog
        fields = '__all__'


class ReportDeliveryLogAdmin(admin.ModelAdmin):
    """Admin configuration for the ReportDeliveryLog model."""

    form = ReportDeliveryLogForm


admin.site.register(ReportDeliveryLog, ReportDeliveryLogAdmin)

# EmailDeliveryLog


class EmailDeliveryLogForm(forms.ModelForm):
    """Form for the EmailDeliveryLog model."""

    class Meta:
        model = EmailDeliveryLog
        fields = '__all__'


class EmailDeliveryLogAdmin(admin.ModelAdmin):
    """Admin configuration for the EmailDeliveryLog model."""

    form = EmailDeliveryLogForm


admin.site.register(EmailDeliveryLog, EmailDeliveryLogAdmin)

# SmsDeliveryLog


class SmsDeliveryLogForm(forms.ModelForm):
    """Form for the SmsDeliveryLog model."""

    class Meta:
        model = SmsDeliveryLog
        fields = '__all__'


class SmsDeliveryLogAdmin(admin.ModelAdmin):
    """Admin configuration for the SmsDeliveryLog model."""

    form = SmsDeliveryLogForm


admin.site.register(SmsDeliveryLog, SmsDeliveryLogAdmin)

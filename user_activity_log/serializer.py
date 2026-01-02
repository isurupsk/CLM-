from rest_framework import serializers
from user_activity_log.models import (
    UserActivityLog, AnalyticalReportList, ReportDeliverySchedule,
    ReportDeliveryLog, EmailDeliveryLog, SmsDeliveryLog
)

# UserActivityLog


class UserActivityLogSerializer(serializers.ModelSerializer):
    """Serializer for the UserActivityLog model."""

    class Meta:
        model = UserActivityLog
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# AnalyticalReportList

class AnalyticalReportListSerializer(serializers.ModelSerializer):
    """Serializer for the AnalyticalReportList model."""

    class Meta:
        model = AnalyticalReportList
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
# ReportDeliverySchedule


class ReportDeliveryScheduleSerializer(serializers.ModelSerializer):
    """Serializer for the ReportDeliverySchedule model."""

    class Meta:
        model = ReportDeliverySchedule
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
# ReportDeliveryLog


class ReportDeliveryLogSerializer(serializers.ModelSerializer):
    """Serializer for the ReportDeliveryLog model."""

    class Meta:
        model = ReportDeliveryLog
        fields = '__all__'

# EmailDeliveryLog


class EmailDeliveryLogSerializer(serializers.ModelSerializer):
    """Serializer for the EmailDeliveryLog model."""

    class Meta:
        model = EmailDeliveryLog
        fields = '__all__'

# SmsDeliveryLog


class SmsDeliveryLogSerializer(serializers.ModelSerializer):
    """Serializer for the SmsDeliveryLog model."""

    class Meta:
        model = SmsDeliveryLog
        fields = '__all__'

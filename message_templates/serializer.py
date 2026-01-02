from rest_framework import serializers
from message_templates.models import (
    NotificationEvent, NotificationPerod,
    EmailTemplate, SmsTemplate, NotificationSchedule
)


class NotificationEventSerializer(serializers.ModelSerializer):
    """Serializer for the NotificationEvent model."""

    class Meta:
        model = NotificationEvent
        fields = '__all__'


class NotificationPerodSerializer(serializers.ModelSerializer):
    """Serializer for the NotificationPerod model."""

    class Meta:
        model = NotificationPerod
        fields = '__all__'


class EmailTemplateSerializer(serializers.ModelSerializer):
    """Serializer for the EmailTemplate model."""

    class Meta:
        model = EmailTemplate
        fields = '__all__'


class SmsTemplateSerializer(serializers.ModelSerializer):
    """Serializer for the SmsTemplate model."""

    class Meta:
        model = SmsTemplate
        fields = '__all__'


class NotificationScheduleSerializer(serializers.ModelSerializer):
    """Serializer for the NotificationSchedule model."""

    class Meta:
        model = NotificationSchedule
        fields = '__all__'

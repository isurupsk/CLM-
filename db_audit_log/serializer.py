from db_audit_log.models import DbAuditLog
from rest_framework import serializers


class DbAuditLogSerializer(serializers.ModelSerializer):
    """Serializer for the DbAuditLog model."""

    class Meta:
        model = DbAuditLog
        fields = '__all__'

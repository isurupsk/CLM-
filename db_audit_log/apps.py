from django.apps import AppConfig


class DbAuditLogConfig(AppConfig):
    """AppConfig for the DbAuditLog app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'db_audit_log'

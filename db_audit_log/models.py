from django.db import models

# Create your models here.

# db_audit_log


class DbAuditLog(models.Model):
    """Model representing the database audit log."""

    db_audit_log_id = models.AutoField(primary_key=True)
    event_description = models.CharField(max_length=200)
    event_date_time = models.DateTimeField()
    event_type = models.CharField(max_length=10)
    user_id = models.IntegerField()
    table_name = models.CharField(max_length=20)
    impacted_row_pk_id = models.IntegerField()
    impacted_column_name = models.CharField(max_length=20)
    old_value = models.CharField(max_length=20)
    new_value = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "1. DbAuditLog"

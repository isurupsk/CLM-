from django.db import models
from django.forms import ValidationError

from contract.models import Contract, CountryContract
from customer_and_user_management.models import Customer
from message_templates.models import NotificationEvent

# Create your models here.


# AwsRegion

class AwsRegion(models.Model):
    """Model representing an AWS region."""

    aws_region_id = models.AutoField(primary_key=True)
    aws_region = models.CharField(max_length=200)
    status = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """raises a ValidationError if any validation fails."""
        if not self.aws_region:
            raise ValidationError('AWS region is required.')

    class Meta:
        verbose_name_plural = "1. AwsRegion"


# CountryAwsRegion

class CountryAwsRegion(models.Model):
    """Model representing an Country Aws Region."""

    country_aws_region_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(CountryContract, on_delete=models.CASCADE, null=False)
    aws_region = models.ForeignKey(
        AwsRegion, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "2. CountryAwsRegion"


# Email
class Email(models.Model):
    """Model representing an Email."""

    email_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    to = models.TextField()
    cc = models.TextField()
    bcc = models.TextField()
    reply_to = models.TextField()
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, null=False)
    notification_event = models.ForeignKey(
        NotificationEvent, on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    from_user = models.CharField(max_length=50)

    def clean(self):
        """raises a ValidationError if any validation fails."""
        if not self.subject:
            raise ValidationError('Email subject is required.')
        if not self.message:
            raise ValidationError('message is required.')
        if not self.to:
            raise ValidationError('TO mail  is required.')

    class Meta:
        verbose_name_plural = "3. Email"


# EmailAttachment

class EmailAttachment(models.Model):
    """Model representing an Email Attachment."""

    email_attachment_id = models.AutoField(primary_key=True)
    file_path = models.TextField()
    email = models.ForeignKey(Email, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def clean(self):
        """raises a ValidationError if any validation fails."""
        if not self.file_path:
            raise ValidationError('file_path is required.')

    class Meta:
        verbose_name_plural = "4. EmailAttachment"

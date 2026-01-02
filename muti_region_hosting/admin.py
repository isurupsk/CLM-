from django import forms
from django.contrib import admin

# Register your models here.
from .models import AwsRegion, CountryAwsRegion, Email, EmailAttachment

admin.site.register(AwsRegion)

# CountryAwsRegion


class CountryAwsRegionForm(forms.ModelForm):
    """Form for creating or updating CountryAwsRegion instances."""

    class Meta:
        model = CountryAwsRegion
        fields = '__all__'


class CountryAwsRegionAdmin(admin.ModelAdmin):
    """Admin configuration for the CountryAwsRegion model."""

    form = CountryAwsRegionForm


admin.site.register(CountryAwsRegion, CountryAwsRegionAdmin)

# Email


class EmailForm(forms.ModelForm):
    """Form for creating or updating Email instances."""

    class Meta:
        model = Email
        fields = '__all__'


class EmailAdmin(admin.ModelAdmin):
    """Admin configuration for the Email model."""

    form = EmailForm


admin.site.register(Email, EmailAdmin)

# EmailAttachment


class EmailAttachmentForm(forms.ModelForm):
    """Form for creating or updating EmailAttachment instances."""

    class Meta:
        model = EmailAttachment
        fields = '__all__'


class EmailAttachmentAdmin(admin.ModelAdmin):
    """Admin configuration for the EmailAttachment model."""

    form = EmailAttachmentForm


admin.site.register(EmailAttachment, EmailAttachmentAdmin)

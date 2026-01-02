from django import forms
from django.contrib import admin
from .models import (
    ContractReviewer, ContractActivityLog, ContractApprover,
    ContractMetadata,  Metadata
)
# ContractReviewer


class ContractReviewerForm(forms.ModelForm):
    """A form for creating and updating ContractReviewer objects."""

    class Meta:
        model = ContractReviewer
        fields = '__all__'


class ContractReviewerAdmin(admin.ModelAdmin):
    """Custom admin interface for managing ContractReviewer objects."""

    form = ContractReviewerForm


admin.site.register(ContractReviewer, ContractReviewerAdmin)


# ContractActivityLog

class ContractActivityLogForm(forms.ModelForm):
    """A form for creating and updating ContractActivityLog objects."""

    class Meta:
        model = ContractActivityLog
        fields = '__all__'


class ContractActivityLogAdmin(admin.ModelAdmin):
    """Custom admin interface for managing ContractActivityLog objects."""

    form = ContractActivityLogForm


admin.site.register(ContractActivityLog, ContractActivityLogAdmin)

# ContractApprover


class ContractApproverForm(forms.ModelForm):
    """A form for creating and updating ContractApprover objects."""

    class Meta:
        model = ContractApprover
        fields = '__all__'


class ContractApproverAdmin(admin.ModelAdmin):
    """Custom admin interface for managing ContractApprover objects."""

    form = ContractApproverForm


admin.site.register(ContractApprover, ContractApproverAdmin)


# Metadata

class MetadataForm(forms.ModelForm):
    """A form for creating and updating Metadata objects."""

    class Meta:
        model = Metadata
        fields = '__all__'


class MetadataAdmin(admin.ModelAdmin):
    """Custom admin interface for managing Metadata objects."""

    form = MetadataForm


admin.site.register(Metadata, MetadataAdmin)

# ContractMetadata


class ContractMetadataForm(forms.ModelForm):
    """A form for creating and updating ContractMetadata objects."""

    class Meta:
        model = ContractMetadata
        fields = '__all__'


class ContractMetadataAdmin(admin.ModelAdmin):
    """Custom admin interface for managing ContractMetadata objects."""

    form = ContractMetadataForm


admin.site.register(ContractMetadata, ContractMetadataAdmin)

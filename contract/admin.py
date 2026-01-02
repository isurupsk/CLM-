from django.contrib import admin
from django import forms
from .models import (
    ContractTemplate, ContractType, ContractAttachment, Contract,
    ContractAuthor, ContractCounterparty, CountryContract, ContractStatus, ContractHistory, )


class CountryAdmin(admin.ModelAdmin):
    """Admin configuration for the Country model."""

    def formfield_for_dbfield(self, db_field, **kwargs):
        """formfield_for_dbfield """
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'country_name':
            formfield.error_messages = {
                'required': 'Please enter a country name.'}
        elif db_field.name == 'status':
            formfield.error_messages = {
                'invalid_choice': 'Please select a valid status.'}
        return formfield


admin.site.register(CountryContract, CountryAdmin)


class ContractTemplateForm(forms.ModelForm):
    """Form for the ContractTemplate model."""

    class Meta:
        model = ContractTemplate
        fields = '__all__'


class ContractTemplateAdmin(admin.ModelAdmin):
    """Admin configuration for the ContractTemplate model."""

    form = ContractTemplateForm


admin.site.register(ContractTemplate, ContractTemplateAdmin)


class ContractTypeForm(forms.ModelForm):
    """Form for the ContractType model."""

    class Meta:
        model = ContractType
        fields = '__all__'


class ContractTypeAdmin(admin.ModelAdmin):
    """Admin configuration for the ContractType model."""

    form = ContractTypeForm


admin.site.register(ContractType, ContractTypeAdmin)


class ContractAttachmentForm(forms.ModelForm):
    """Form for the ContractAttachment model."""

    class Meta:
        model = ContractAttachment
        fields = '__all__'


class ContractAttachmentAdmin(admin.ModelAdmin):
    """Admin configuration for the ContractAttachment model."""

    form = ContractAttachmentForm


admin.site.register(ContractAttachment, ContractAttachmentAdmin)


class ContractForm(forms.ModelForm):
    """Form for the Contract model."""

    class Meta:
        model = Contract
        fields = '__all__'


class ContractAdmin(admin.ModelAdmin):
    """Admin configuration for the Contract model."""

    form = ContractForm


admin.site.register(Contract, ContractAdmin)


class ContractStatusForm(forms.ModelForm):
    """Form for the ContractStatus model."""

    class Meta:
        model = ContractStatus
        fields = '__all__'


class ContractStatusAdmin(admin.ModelAdmin):
    """Admin configuration for the ContractStatus model."""

    form = ContractStatusForm


admin.site.register(ContractStatus, ContractStatusAdmin)


class ContractHistoryForm(forms.ModelForm):
    """Form for the ContractHistory model."""

    class Meta:
        model = ContractHistory
        fields = '__all__'


class ContractHistoryAdmin(admin.ModelAdmin):
    """Admin configuration for the ContractHistory model."""

    form = ContractHistoryForm


admin.site.register(ContractHistory, ContractHistoryAdmin)

admin.site.register(ContractAuthor)
admin.site.register(ContractCounterparty)

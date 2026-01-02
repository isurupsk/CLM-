from django.db import models

# Create your models here.


from contract.models import Contract, ContractStatus
from customer_and_user_management.models import Customer, User

# UploadContract


class UploadContract(models.Model):
    """Model representing a Upload Contract."""

    uploaded_contract_id = models.AutoField(primary_key=True)
    uploaded_user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_contract_state = models.ForeignKey(
        ContractStatus, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    uploaded_date = models.DateTimeField()
    contract_source_type = models.CharField(max_length=20)
    contract_source_address = models.CharField(max_length=50)
    contract_destination_address = models.CharField(max_length=50)
    contract_upload_status = models.CharField(max_length=20)
    contract_upload_filure_reasons = models.CharField(max_length=20)
    metadata_source_type = models.CharField(max_length=20)
    metadata_source_address = models.CharField(max_length=50)
    metadata_destination_address = models.CharField(max_length=50)
    metadata_upload_status = models.CharField(max_length=20)
    metadata_upload_filure_reasons = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "1. UploadContract"

# RenewContract


class RenewContract(models.Model):
    """Model representing a renewed contract."""

    renew_contract_id = models.AutoField(primary_key=True)
    renewed_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    renewed_data = models.DateTimeField()
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    # old_contract_id = models.ForeignKey('Language', on_delete=models.CASCADE)
    # new_contract_id = models.ForeignKey('Language', on_delete=models.CASCADE)
    remarks = models.CharField(max_length=20)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "2. RenewContract"

# UploadedContractStatus


class UploadedContractStatus(models.Model):
    """Model representing the status of an uploaded contract."""

    uploaded_contract_status_id = models.AutoField(primary_key=True)
    uploaded_contract_state = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "3. UploadedContractStatus"

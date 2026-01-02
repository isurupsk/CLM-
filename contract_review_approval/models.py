from django.db import models
from django.core.exceptions import ValidationError
from customer_and_user_management.models import User, Customer
from contract.models import Contract
from django.db.models import UniqueConstraint
     
# ContractReviewer

class ContractReviewer(models.Model):
    """Model representing a contract reviewer."""

    contract_reviewer_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review_status = models.IntegerField()
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    review_order = models.IntegerField(unique=True)
    internal_or_external = models.CharField(max_length=10)
    remarks = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['contract_id', 'review_order'],
                name='unique_contract_review_order_reviewer'
            )
        ]

    def save(self, *args, **kwargs):
        if self.is_current and self.is_completed:
            raise ValidationError("Both 'is_current' and 'is_completed' cannot be True at the same time.")

        if self.is_current:
            # Set all other instances with is_current=True to False for the same contract
            ContractReviewer.objects.filter(contract_id=self.contract_id, is_current=True).exclude(pk=self.pk).update(is_current=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"ContractReviewer {self.contract_reviewer_id}"
    
    def clean(self):
        """Raises ValidationError if any validation fails."""
        if not self.review_order:
            raise ValidationError('Review order is required.')
        if not self.review_status:
            raise ValidationError('Review status is required.')
        if not self.internal_or_external:
            raise ValidationError('Internal or external is required.')




# ContractActivityLog

class ContractActivityLog(models.Model):
    """Model representing a contract activity log."""

    contract_activity_log_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    activity = models.CharField(max_length=255)
    activity_time = models.DateTimeField(null=False)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False)

# back-end validation shema

    def clean(self):
        """Raises ValidationError if any validation fails."""
        if not self.activity:
            raise ValidationError('Activity  is required.')
        if not self.activity_time:
            raise ValidationError('Activity time is required.')



# ContractApprover

# class ContractApprover(models.Model):
#     contract_approver_id = models.IntegerField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#     contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
#     review_order = models.IntegerField()
#     approve_status = models.IntegerField()
#     internal_or_external = models.CharField(max_length=10)
#     remarks = models.CharField(max_length=255)
#     is_completed = models.BooleanField(default=False)
#     is_current = models.BooleanField(default=False)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     def save(self, *args, **kwargs):
#         if self.is_current and self.is_completed:
#             raise ValidationError("Both 'is_current' and 'is_completed' cannot be True at the same time.")
#         super().save(*args, **kwargs)

#         if self.is_current:
#             ContractApprover.objects.filter(contract_id=self.contract_id, review_order=self.review_order).exclude(pk=self.pk).update(is_current=False)
#         elif self.is_completed:
#             ContractApprover.objects.filter(contract_id=self.contract_id, review_order=self.review_order).exclude(pk=self.pk).update(is_completed=False)

#     def __str__(self):
#         return f"ContractApprover {self.contract_approver_id}"

# Working 
# from django.db.models import UniqueConstraint

# class ContractApprover(models.Model):
#     contract_approver_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
#     review_order = models.IntegerField()
#     approve_status = models.IntegerField()
#     internal_or_external = models.CharField(max_length=10)
#     remarks = models.CharField(max_length=255)
#     is_completed = models.BooleanField(default=False)
#     is_current = models.BooleanField(default=False)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

#     class Meta:
#         constraints = [
#             UniqueConstraint(
#                 fields=['contract_id', 'review_order'],
#                 name='unique_contract_review_order'
#             )
#         ]

#     def save(self, *args, **kwargs):
#         if self.is_current and self.is_completed:
#             raise ValidationError("Both 'is_current' and 'is_completed' cannot be True at the same time.")

#         if self.is_current:
#             ContractApprover.objects.filter(contract_id=self.contract_id, is_current=True).exclude(pk=self.pk).update(is_current=False)

#         if self.is_completed:
#             ContractApprover.objects.filter(contract_id=self.contract_id, is_completed=True).exclude(pk=self.pk).update(is_completed=False)

#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"ContractApprover {self.contract_approver_id}"
    
#     def clean(self):
#         """Raises ValidationError if any validation fails."""
#         if not self.review_order:
#             raise ValidationError('Review order is required.')
#         if not self.approve_status:
#             raise ValidationError('Approve status is required.')
#         if not self.internal_or_external:
#             raise ValidationError('Internal or external is required.')
#         if not self.created_at:
#             raise ValidationError('Created at Date is required.')

# Working end 

# Working 2

class ContractApprover(models.Model):
    contract_approver_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    review_order = models.IntegerField()
    approve_status = models.IntegerField()
    internal_or_external = models.CharField(max_length=10)
    remarks = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['contract_id', 'review_order'],
                name='unique_contract_review_order_approver'
            )
        ]

    def save(self, *args, **kwargs):
        if self.is_current and self.is_completed:
            raise ValidationError("Both 'is_current' and 'is_completed' cannot be True at the same time.")

        if self.is_current:
            # Set all other instances with is_current=True to False for the same contract
            ContractApprover.objects.filter(contract_id=self.contract_id, is_current=True).exclude(pk=self.pk).update(is_current=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"ContractApprover {self.contract_approver_id}"
    
    def clean(self):
        """Raises ValidationError if any validation fails."""
        if not self.review_order:
            raise ValidationError('Review order is required.')
        if not self.approve_status:
            raise ValidationError('Approve status is required.')
        if not self.internal_or_external:
            raise ValidationError('Internal or external is required.')
 



# Working 2

# Test 1 

# Test 2 






    # def save(self, *args, **kwargs):
    #     if self.is_current and self.is_completed:
    #         raise ValidationError("Both 'is_current' and 'is_completed' cannot be True at the same time.")
    #     super().save(*args, **kwargs)

    #     if self.is_current:
    #         ContractApprover.objects.exclude(pk=self.pk).update(is_current=False)
    #     elif self.is_completed:
    #         ContractApprover.objects.exclude(pk=self.pk).update(is_completed=False)

    # def __str__(self):
    #     return f"ContractApprover {self.contract_approver_id}"

# ContractMetadata


class ContractMetadata(models.Model):
    """Model representing a Contract Metadata log."""

    contract_metadata_id = models.AutoField(primary_key=True)
    metadata_id = models.ForeignKey('Metadata', on_delete=models.CASCADE)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    added_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    metadata_value = models.CharField(max_length=255)
    additional_meta_tag_id = models.CharField(
        max_length=255)  # Add this attribute

# back-end validation shema

    def clean(self):
        """Raises ValidationError if any validation fails."""
        if not self.created_at:
            raise ValidationError('Create Date is required.')


# Metadata

class Metadata(models.Model):
    """Model representing a Metadata log."""

    metadata_id = models.AutoField(primary_key=True)
    metadata_key = models.CharField(max_length=20)
    created_date = models.DateTimeField(null=False)
    created_by_user_id = models.IntegerField(null=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# back-end validation shema

    def clean(self):
        """Raises ValidationError if any validation fails."""
        if not self.metadata_key:
            raise ValidationError('Metadata key  is required.')


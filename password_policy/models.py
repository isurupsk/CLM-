from django.db import models

# Create your models here.


from customer_and_user_management.models import Customer

# PasswordPolicyRule


class PasswordPolicyRule(models.Model):
    """Model representing a Password Policy Rule."""

    password_policy_rule_id = models.AutoField(primary_key=True)
    possword_policy_rule = models.CharField(max_length=40)
    answer_type = models.CharField(max_length=10)
    possible_answers = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "1. PasswordPolicyRule"

# PasswordPolicy


class PasswordPolicy(models.Model):
    """Model representing a password policy."""

    password_policy_id = models.AutoField(primary_key=True)
    password_policy_rule = models.ForeignKey(
        PasswordPolicyRule, on_delete=models.CASCADE)
    answer = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "2. PasswordPolicy"

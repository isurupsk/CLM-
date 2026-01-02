from rest_framework import serializers
from password_policy.models import PasswordPolicy, PasswordPolicyRule


class PasswordPolicyRuleSerializer(serializers.ModelSerializer):
    """Serializer for the PasswordPolicyRule model."""

    class Meta:
        model = PasswordPolicyRule
        fields = '__all__'


class PasswordPolicySerializer(serializers.ModelSerializer):
    """Serializer for the PasswordPolicy model."""

    password_policy_rule = PasswordPolicyRuleSerializer(read_only=True)

    class Meta:
        model = PasswordPolicy
        exclude = ('customer',)

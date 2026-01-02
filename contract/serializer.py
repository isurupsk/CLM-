from rest_framework import serializers
from contract.models import (
    ContractAttachment, ContractAuthor, ContractCounterparty,
    ContractHistory, ContractStatus, ContractTemplate, ContractType, CountryContract, Contract
)

# ContractTemplateSerializer


class ContractTemplateSerializer(serializers.ModelSerializer):
    """Serializer for the ContractTemplate model."""

    class Meta:
        model = ContractTemplate
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# ContractTypeSerializer


class ContractTypeSerializer(serializers.ModelSerializer):
    """Serializer for the ContractType model."""

    class Meta:
        model = ContractType
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# ContractAttachmentSerializer


class ContractAttachmentSerializer(serializers.ModelSerializer):
    """Serializer for the ContractAttachment model."""

    class Meta:
        model = ContractAttachment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# Contract


class ContractSerializer(serializers.ModelSerializer):
    """Serializer for the Contract model."""

    class Meta:
        model = Contract
        fields = '__all__'
        # read_only_fields = ('created_at', 'updated_at')
# ContractAuthor


class ContractAuthorSerializer(serializers.ModelSerializer):
    """Serializer for the ContractAuthor model."""

    class Meta:
        model = ContractAuthor
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
# ContractCounterparty


class ContractCounterpartySerializer(serializers.ModelSerializer):
    """Serializer for the ContractCounterparty model."""

    class Meta:
        model = ContractCounterparty
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
# CountrySerializer


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for the Country model."""

    class Meta:
        model = CountryContract
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
# ContractStatusSerializer


class ContractStatusSerializer(serializers.ModelSerializer):
    """Serializer for the ContractStatus model."""

    class Meta:
        model = ContractStatus
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
# ContractHistorySerializer


class ContractHistorySerializer(serializers.ModelSerializer):
    """Serializer for the ContractHistory model."""

    class Meta:
        model = ContractHistory
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


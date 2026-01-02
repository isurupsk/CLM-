from rest_framework import serializers
from contract_review_approval.models import (
    ContractActivityLog, ContractApprover, Metadata,
    ContractMetadata, ContractReviewer
)


class ContractReviewerSerializer(serializers.ModelSerializer):
    """Serializer for the ContractReviewer model."""

    class Meta:
        model = ContractReviewer
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ContractActivityLogSerializer(serializers.ModelSerializer):
    """Serializer for the ContractActivityLog model."""

    class Meta:
        model = ContractActivityLog
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ContractApproverSerializer(serializers.ModelSerializer):
    """Serializer for the ContractApprover model."""

    class Meta:
        model = ContractApprover
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class MetadataSerializer(serializers.ModelSerializer):
    """Serializer for the Metadata model."""

    class Meta:
        model = Metadata
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class ContractMetadataSerializer(serializers.ModelSerializer):
    """Serializer for the ContractMetadata model."""

    class Meta:
        model = ContractMetadata
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
from rest_framework import serializers
from muti_region_hosting.models import (
    AwsRegion, CountryAwsRegion, Email, EmailAttachment
)


class AwsRegionSerializer(serializers.ModelSerializer):
    """Serializer for the AwsRegion model."""

    class Meta:
        model = AwsRegion
        fields = '__all__'


class CountryAwsRegionSerializer(serializers.ModelSerializer):
    """Serializer for the CountryAwsRegion model."""

    country_name = serializers.ReadOnlyField(source='country.country_name')
    aws_region = AwsRegionSerializer()

    class Meta:
        model = CountryAwsRegion
        fields = ['country_name', 'aws_region']


class EmailAttachmentSerializer(serializers.ModelSerializer):
    """Serializer for the EmailAttachment model."""

    class Meta:
        model = EmailAttachment
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    """Serializer for the EmailSerializer model."""

    attachments = EmailAttachmentSerializer(many=True)

    class Meta:
        model = Email
        fields = '__all__'

    def create(self, validated_data):
        """Create a new instance of the Email model."""

        attachments_data = validated_data.pop('attachments')
        email = Email.objects.create(**validated_data)
        for attachment_data in attachments_data:
            EmailAttachment.objects.create(email=email, **attachment_data)
        return email

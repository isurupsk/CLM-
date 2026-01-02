from master_data.models import Currency, DateFormat, Language
from rest_framework import serializers


# Language

class LanguageSerializer(serializers.ModelSerializer):
    """Serializer for the Language model."""

    class Meta:
        model = Language
        fields = '__all__'

# Currency


class CurrencySerializer(serializers.ModelSerializer):
    """Serializer for the Currency model."""

    class Meta:
        model = Currency
        fields = '__all__'

# DateFormat


class DateFormatSerializer(serializers.ModelSerializer):
    """Serializer for the DateFormat model."""

    class Meta:
        model = DateFormat
        fields = '__all__'

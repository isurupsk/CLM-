from django.db import models


# Language

class Language(models.Model):
    """Model representing a Language."""

    language_id = models.AutoField(primary_key=True)
    language_code = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.language

    class Meta:
        verbose_name_plural = "1. Language"


# Currency

class Currency(models.Model):
    """Model representing a Currency."""

    currency_id = models.AutoField(primary_key=True)
    currency_code = models.CharField(max_length=30)
    currency = models.CharField(max_length=30, default='USD')
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.currency

    class Meta:
        verbose_name_plural = "2. Currency"


# DateFormat

class DateFormat(models.Model):
    """Model representing a date format."""

    date_format_id = models.AutoField(primary_key=True)
    date_format = models.CharField(max_length=30)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    ############ Anura 20/06/2023 #############
    def __str__(self):
        return self.date_format
    ################### End ###################

    class Meta:
        verbose_name_plural = "3. DateFormat"

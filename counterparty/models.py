from django.db import models

from customer_and_user_management.models import User, Customer,Country
# Countryparty


class Counterparty(models.Model):
    """Model representing a counterparty."""
    counterparty_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    company_web = models.CharField(max_length=100)
    company_address = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    company_contact_number = models.CharField(max_length=14)
    ################## Anura 21/06/2023 #########################
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100)
    email = models.EmailField()
    ########################## End ##############################
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

# CustomerCounterpartyContract


class CustomerCounterpartyContact(models.Model):
    """Model representing a customer counterparty contract."""
    customer_counterparty_contact_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True)
    counterparty_contact_id = models.ForeignKey(
        'CounterpartyContact', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# CounterpartyContract


class CounterpartyContact(models.Model):
    """Model representing a contact for a counterparty."""
    counterparty_contact_id = models.AutoField(primary_key=True)
    counterparty_id = models.ForeignKey(Counterparty, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ################## Anura 20/06/2023 #########################
    is_primary = models.BooleanField()
    ########################## End ##############################
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    ################## Anura 20/06/2023 #########################
    def save(self, *args, **kwargs):
        if self.is_primary:
            CounterpartyContact.objects.filter(counterparty_id=self.counterparty_id, is_primary=True).exclude(pk=self.pk).update(is_primary=False)
        super().save(*args, **kwargs) 
    ########################## End ##############################

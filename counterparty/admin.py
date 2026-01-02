from django.contrib import admin

# Register your models here.
from .models import Counterparty, CustomerCounterpartyContact, CounterpartyContact


admin.site.register(Counterparty)
admin.site.register(CustomerCounterpartyContact)
admin.site.register(CounterpartyContact)

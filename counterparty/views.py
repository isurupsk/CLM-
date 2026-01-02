from counterparty import serializer
from counterparty.models import (
    Counterparty, CounterpartyContact, CustomerCounterpartyContact
)
from rest_framework import generics
from django.db.models import Count

# Create your views here.


# Counterparty

# ListView
class CounterpartyListView(generics.ListAPIView):
    """View for retrieving the Counterparty List."""

    serializer_class = serializer.CountrypartySerializer
    
    ############## Anura 20/06/2023 ##############
    # queryset = Counterparty.objects.all()
    queryset = Counterparty.objects.annotate(user_count=Count('counterpartycontact'))
    ############## End ##############

# OneView


class CounterpartyOneView(generics.RetrieveAPIView):
    """View for retrieving the Counterparty entry."""

    serializer_class = serializer.CountrypartySerializer

    queryset = Counterparty.objects.all()

# CreateView


class CounterpartyCreateView(generics.CreateAPIView):
    """View for retrieving the Counterparty Create."""

    serializer_class = serializer.CountrypartySerializer

    queryset = Counterparty.objects.all()

# UpdateView


class CounterpartyUpdateView(generics.UpdateAPIView):
    """View for retrieving the Counterparty Update."""

    serializer_class = serializer.CountrypartySerializer

    queryset = Counterparty.objects.all()

# DeleteView


class CounterpartyDeleteView(generics.DestroyAPIView):
    """View for retrieving the Counterparty Delete."""

    serializer_class = serializer.CountrypartySerializer

    queryset = Counterparty.objects.all()

# Counterparties By Customer View


class CounterpartiesByCustomerView(generics.ListAPIView):
    """View for retrieving Create Counterparties By Customer View."""

    serializer_class = serializer.CountrypartySerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Counterparty.objects.filter(customer_id=customer_id)

# CustomerCounterpartyContact

# ListView


class CustomerCounterpartyContactListView(generics.ListAPIView):
    """View for retrieving the CustomerCounterpartyContact List."""

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()

# OneView


class CustomerCounterpartyContactOneView(generics.RetrieveAPIView):
    """View for retrieving the CustomerCounterpartyContact entry."""

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()

# CreateView


class CustomerCounterpartyContactCreateView(generics.CreateAPIView):
    """View for retrieving the CustomerCounterpartyContact Create."""

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()

# UpdateView


class CustomerCounterpartyContactUpdateView(generics.UpdateAPIView):
    """View for retrieving the CustomerCounterpartyContact Update."""

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()

# DeleteView


class CustomerCounterpartyContactDeleteView(generics.DestroyAPIView):
    """View for retrieving the CustomerCounterpartyContact Delete."""

    serializer_class = serializer.CustomerCounterpartyContractSerializer

    queryset = CustomerCounterpartyContact.objects.all()


# CounterpartyContract

# ListView
class CounterpartyContractListView(generics.ListAPIView):
    """View for retrieving the CounterpartyContract List."""

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()

# OneView


class CounterpartyContractOneView(generics.RetrieveAPIView):
    """View for retrieving the CounterpartyContract entry."""

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()

# CreateView


class CounterpartyContractCreateView(generics.CreateAPIView):
    """View for retrieving the CounterpartyContract Create."""

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()

# UpdateView


class CounterpartyContractUpdateView(generics.UpdateAPIView):
    """View for retrieving the CounterpartyContract Update."""

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()

# DeleteView


class CounterpartyContractDeleteView(generics.DestroyAPIView):
    """View for retrieving the CounterpartyContract Delete."""

    serializer_class = serializer.CounterpartyContractSerializer

    queryset = CounterpartyContact.objects.all()
############################ Janitha 07.06 ###############################

class RetrieveAllCounterpartyContactView(generics.ListAPIView):
    serializer_class = serializer.CounterpartyContractSerializer

    def get_queryset(self):
        counterparty_id = self.kwargs['counterparty_id']
        return CounterpartyContact.objects.filter(counterparty_id=counterparty_id)

############################ End ##########################################
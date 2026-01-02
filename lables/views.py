from lables import serializer
from lables.models import (
    ContractLabel,
    LabelMaster
)
from rest_framework import generics
from django.db.models import Count

########################### Anura 21/06/2023 ##########################
# Counterparties By Customer View
class LabelsByCustomerView(generics.ListAPIView):
    """View for retrieving labels By Customer View."""

    serializer_class = serializer.LabelMasterSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return LabelMaster.objects.filter(customer_id=customer_id)
       
################################# End #################################

######################### Janitha 06.30 #####################################
class ContractLabelByContractView(generics.ListAPIView):
    """View for retrieving the label list for a given contract."""

    serializer_class = serializer.ContractLabelSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractLabel.objects.filter(contract_id=contract_id)

########################## End #############################################
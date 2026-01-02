
from contract import serializer
from contract.models import (
    Contract, ContractAttachment, ContractAuthor, ContractCounterparty,
    ContractHistory, ContractStatus, ContractTemplate, ContractType, CountryContract
)
from rest_framework import generics
from rest_framework.exceptions import ValidationError

import boto3
from botocore.exceptions import NoCredentialsError
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from .models import ContractAttachment
from .serializer import ContractAttachmentSerializer, ContractHistorySerializer, ContractTemplateSerializer


from botocore.exceptions import ClientError
from django.conf import settings

# Create your views here.


# ContractTemplate

# ListView
class ContractTemplateListView(generics.ListAPIView):
    """View for retrieving the ContractTemplate List."""

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()

# OneView


class ContractTemplateOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractTemplate entry."""

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()

# CreateView


class ContractTemplateCreateView(generics.CreateAPIView):
    """View for retrieving the ContractTemplate Create."""

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()

# UpdateView


class ContractTemplateUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractTemplate Update."""

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()

# DeleteView


class ContractTemplateDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractTemplate Delete."""

    serializer_class = serializer.ContractTemplateSerializer

    queryset = ContractTemplate.objects.all()

##################### Janitha 07.06 #######################

class RetrieveAllContractTemplateView(generics.ListAPIView):
    serializer_class = ContractTemplateSerializer

    def get_queryset(self):
        contract_type = self.kwargs['contract_type']
        return ContractTemplate.objects.filter(contract_type=contract_type)

######################## End ###############################


# ContractType

# ListView
class ContractTypeListView(generics.ListAPIView):
    """View for retrieving the ContractType List."""

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()

# OneView


class ContractTypeOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractType entry."""

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()

# CreateView


class ContractTypeCreateView(generics.CreateAPIView):
    """View for retrieving the ContractType Creat."""

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()

# UpdateView


class ContractTypeUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractType Update."""

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()

# DeleteView


class ContractTypeDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractType Delete."""

    serializer_class = serializer.ContractTypeSerializer

    queryset = ContractType.objects.all()


# ContractAttachment

# ListView
class ContractAttachmentListView(generics.ListAPIView):
    """View for retrieving the ContractAttachment List."""

    serializer_class = serializer.ContractAttachmentSerializer

    queryset = ContractAttachment.objects.all()

# OneView


class ContractAttachmentOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractAttachment entry."""

    serializer_class = serializer.ContractAttachmentSerializer

    queryset = ContractAttachment.objects.all()

# CreateView
class ContractAttachmentCreateView(generics.CreateAPIView):
    """View for creating a ContractAttachment."""
    serializer_class = ContractAttachmentSerializer
    queryset = ContractAttachment.objects.all()

    def perform_create(self, serializer):
        # Save the file path in the model
        serializer.save(user=self.request.user)

def create(self, request, *args, **kwargs):
    # Upload the file to AWS S3
    file = request.FILES.get('file_path')
    if file:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        try:
            # Open the file in binary mode and upload it
            with open(file.temporary_file_path(), 'rb') as f:
                s3_client.upload_fileobj(f, settings.AWS_S3_BUCKET_NAME, file.name)

            # Save the file path in the model
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ClientError as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        raise ValidationError('No file uploaded')

# UpdateView


class ContractAttachmentUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractAttachment Update."""

    serializer_class = serializer.ContractAttachmentSerializer

    queryset = ContractAttachment.objects.all()

# DeleteView


class ContractAttachmentDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractAttachment Delete."""

    serializer_class = serializer.ContractAttachmentSerializer

    queryset = ContractAttachment.objects.all()


# Contract

# ListView
class ContractListView(generics.ListAPIView):
    """View for retrieving the Contract List."""

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# OneView


class ContractOneView(generics.RetrieveAPIView):
    """View for retrieving the Contract entry."""

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# CreateView


class ContractCreateView(generics.CreateAPIView):
    """View for retrieving the Contract Create."""

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# UpdateView


class ContractUpdateView(generics.UpdateAPIView):
    """View for retrieving the Contract Update."""

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# DeleteView


class ContractDeleteView(generics.DestroyAPIView):
    """View for retrieving the Contract Delete."""

    serializer_class = serializer.ContractSerializer

    queryset = Contract.objects.all()

# Contract by status


class ContractsByStatusView(generics.ListAPIView):
    """API view to retrieve Contract by status."""

    serializer_class = serializer.ContractSerializer

    def get_queryset(self):
        """Retrieve Contracts based on the provided status ID."""
        # Assuming you pass the status ID in the URL
        status_id = self.kwargs['status_id']
        return Contract.objects.filter(contract_status=status_id)

# ContractsByStatusAndCustomerView


class ContractsByStatusAndCustomerView(generics.ListAPIView):
    """API view to retrieve contract by Status And Customer."""

    serializer_class = serializer.ContractSerializer

    def get_queryset(self):
        """Retrieve Contracts based on the provided status ID and customer ID."""
        customer_id = self.kwargs['customer_id']
        status_id = self.kwargs['status_id']
        return Contract.objects.filter(customer_id=customer_id, contract_status_id=status_id)

# ContractsByCustomerView


class ContractsByCustomerView(generics.ListAPIView):
    """API view to retrieve contract by Custome ID."""

    serializer_class = serializer.ContractSerializer

    def get_queryset(self):
        """API view to retrieve contract by Custome ID."""
        customer_id = self.kwargs['customer_id']
        return Contract.objects.filter(customer_id=customer_id)

# ContractAuthorsByContractView


class ContractAuthorsByContractView(generics.ListAPIView):
    """API view to retrieve ContractAuthors by contract ID."""

    serializer_class = serializer.ContractAuthorSerializer

    def get_queryset(self):
        """API view to retrieve ContractAuthors by contract ID."""
        contract_id = self.kwargs['contract_id']
        return ContractAuthor.objects.filter(contract_id=contract_id)

# Contract History


class ContractVersionsByContractView(generics.ListAPIView):
    """API view to retrieve Contract History by contract ID."""

    serializer_class = serializer.ContractHistorySerializer

    def get_queryset(self):
        """API view to retrieve Contract History by contract ID."""
        contract_id = self.kwargs['contract_id']
        return ContractHistory.objects.filter(contract_id=contract_id)

# Contract Attachment


class ContractAttachmentsByContractView(generics.ListAPIView):
    """API view to retrieve contract attachments by contract ID."""

    serializer_class = serializer.ContractAttachmentSerializer

    def get_queryset(self):
        """Retrieve contract attachments based on the provided contract ID."""
        contract_id = self.kwargs['contract_id']
        return ContractAttachment.objects.filter(contract_id=contract_id)
    
####################### Janitha 06.30 ##########################
#ContractAttachment By Contract
class ContractAttachmentByContractView(generics.ListAPIView):
    """View for retrieving attachments for a given contract."""

    serializer_class = serializer.ContractAttachmentSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractAttachment.objects.filter(contract_id=contract_id)
####################### End ######################################


# ContractAuthor

# ListView
class ContractAuthorListView(generics.ListAPIView):
    """View for retrieving the ContractAuthor list."""

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()

# OneView


class ContractAuthorOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractAuthor entry."""

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()

# CreateView


class ContractAuthorCreateView(generics.CreateAPIView):
    """View for retrieving the ContractAuthor Create."""

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()

# UpdateView


class ContractAuthorUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractAuthor  Update."""

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()

# DeleteView


class ContractAuthorDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractAuthor Delete."""

    serializer_class = serializer.ContractAuthorSerializer

    queryset = ContractAuthor.objects.all()


# ContractCounterparty

# ListView
class ContractCounterpartyListView(generics.ListAPIView):
    """View for retrieving the ContractCounterparty list."""

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()

# OneView


class ContractCounterpartyOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractCounterparty entry."""

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()

# CreateView


class ContractCounterpartyCreateView(generics.CreateAPIView):
    """View for retrieving the ContractCounterparty Create."""

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()

# UpdateView


class ContractCounterpartyUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractCounterparty Update."""

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()

# DeleteView


class ContractCounterpartyDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractCounterparty Delete."""

    serializer_class = serializer.ContractCounterpartySerializer

    queryset = ContractCounterparty.objects.all()


# Country

# ListView
class CountryListView(generics.ListAPIView):
    """View for retrieving the Country list."""

    serializer_class = serializer.CountrySerializer

    queryset = CountryContract.objects.all()

# OneView


class CountryOneView(generics.RetrieveAPIView):
    """View for retrieving the Country entry."""

    serializer_class = serializer.CountrySerializer

    queryset = CountryContract.objects.all()

# CreateView


class CountryCreateView(generics.CreateAPIView):
    """View for retrieving the Country Create."""

    serializer_class = serializer.CountrySerializer

    queryset = CountryContract.objects.all()

# UpdateView


class CountryUpdateView(generics.UpdateAPIView):
    """View for retrieving the Country Update."""

    serializer_class = serializer.CountrySerializer

    queryset = CountryContract.objects.all()

# DeleteView


class CountryDeleteView(generics.DestroyAPIView):
    """View for retrieving the Country Delete."""

    serializer_class = serializer.CountrySerializer

    queryset = CountryContract.objects.all()


# ContractStatus

# ListView
class ContractStatusListView(generics.ListAPIView):
    """View for retrieving the ContractStatus list."""

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()

# OneView


class ContractStatusOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractStatus entry."""

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()

# CreateView


class ContractStatusCreateView(generics.CreateAPIView):
    """View for retrieving the ContractStatus Create."""

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()

# UpdateView


class ContractStatusUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractStatus Update."""

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()

# DeleteView


class ContractStatusDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractStatus Delete."""

    serializer_class = serializer.ContractStatusSerializer

    queryset = ContractStatus.objects.all()


# ContractHistory

# ListView
class ContractHistoryListView(generics.ListAPIView):
    """View for retrieving the contract history list."""

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()

# OneView


class ContractHistoryOneView(generics.RetrieveAPIView):
    """View for retrieving a single contract history entry."""

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()

# CreateView


class ContractHistoryCreateView(generics.CreateAPIView):
    """View for retrieving a single contract history Create."""

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()

# UpdateView


class ContractHistoryUpdateView(generics.UpdateAPIView):
    """View for retrieving a single contract history Update."""

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()

# DeleteView


class ContractHistoryDeleteView(generics.DestroyAPIView):
    """View for retrieving a single contract history Delete."""

    serializer_class = serializer.ContractHistorySerializer

    queryset = ContractHistory.objects.all()

#################### Janitha 07.06 ##############################

class RetrieveAllContractHistoryView(generics.ListAPIView):
    serializer_class = ContractHistorySerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractHistory.objects.filter(contract_id=contract_id)

################## End #############################################

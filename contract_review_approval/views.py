from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from contract_review_approval import serializer
from contract_review_approval.models import (
    ContractActivityLog, ContractApprover, ContractMetadata,
    ContractReviewer, Metadata
)


# Create your views here.

# ContractReviewer

# ListView


class ContractReviewerListView(generics.ListAPIView):
    """View for retrieving the ContractReviewer List."""

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()

# OneView


class ContractReviewerOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractReviewer entry."""

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()

# CreateView


class ContractReviewerCreateView(generics.CreateAPIView):
    """View for retrieving the ContractReviewer Create."""

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()

# UpdateView


class ContractReviewerUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractReviewer Update."""

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()

# DeleteView


class ContractReviewerDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractReviewer Delete."""

    serializer_class = serializer.ContractReviewerSerializer

    queryset = ContractReviewer.objects.all()


# Contract Reviewers By ContractView

class ContractReviewersByContractView(generics.ListAPIView):
    """View for retrieving contract reviewers for a specific contract."""

    serializer_class = serializer.ContractReviewerSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractReviewer.objects.filter(contract_id=contract_id)
    
###################### Anura 30/06/2023 ##########################
class ContractRevieverCompletedView(generics.ListAPIView):
    """View for retrieving the ContractApprover completed List."""
    
    queryset = ContractReviewer.objects.filter(is_completed=True)
    serializer_class = serializer.ContractReviewerSerializer

class ContractRevieverCurrentView(generics.ListAPIView):
    """View for retrieving the ContractApprover current List."""
    
    queryset = ContractReviewer.objects.filter(is_current=True)
    serializer_class = serializer.ContractReviewerSerializer
############################# End ################################

######################### Janitha 07.06 #################################

class RetrieveAllContractReviewerView(generics.ListAPIView):
    serializer_class = serializer.ContractReviewerSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractReviewer.objects.filter(contract_id=contract_id)

######################### End ############################################

# ContractActivityLog

# ListView


class ContractActivityLogListView(generics.ListAPIView):
    """View for retrieving the ContractActivityLog List."""

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()

# OneView


class ContractActivityLogOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractActivityLog entry."""

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()

# CreateView


class ContractActivityLogCreateView(generics.CreateAPIView):
    """View for retrieving the ContractActivityLog Create."""

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()

# UpdateView


class ContractActivityLogUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractActivityLog Update."""

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()

# DeleteView


class ContractActivityLogDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractActivityLog Delete."""

    serializer_class = serializer.ContractActivityLogSerializer

    queryset = ContractActivityLog.objects.all()


# ContractApprover

# ListView
class ContractApproverListView(generics.ListAPIView):
    """View for retrieving the ContractApprover List."""

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()

#################### Anura 30/06/2023 ####################
# CompletedListView
class ContractApproverCompletedView(generics.ListAPIView):
    """View for retrieving the ContractApprover completed List."""
    
    queryset = ContractApprover.objects.filter(is_completed=True)
    serializer_class = serializer.ContractApproverSerializer

class ContractApproverCurrentView(generics.ListAPIView):
    """View for retrieving the ContractApprover current List."""
    
    queryset = ContractApprover.objects.filter(is_current=True)
    serializer_class = serializer.ContractApproverSerializer

########################### End ##########################

# OneView


class ContractApproverOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractApprover entry."""

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()

# CreateView


class ContractApproverCreateView(generics.CreateAPIView):
    """View for retrieving the ContractApprover Create."""

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()

# UpdateView


class ContractApproverUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractApprover Update."""

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()

# DeleteView


class ContractApproverDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractApprover Delete."""

    serializer_class = serializer.ContractApproverSerializer

    queryset = ContractApprover.objects.all()


# Contract Approvers By ContractView


class ContractApproversByContractView(generics.ListAPIView):
    """View for retrieving ontract Approvers By ContractView."""
    serializer_class = serializer.ContractApproverSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ContractApprover.objects.filter(contract_id=contract_id)


# Metadata

# ListView
class MetadataListView(generics.ListAPIView):
    """View for retrieving the Metadata List."""

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()

# OneView


class MetadataOneView(generics.RetrieveAPIView):
    """View for retrieving the Metadata entry."""

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()

# CreateView


class MetadataCreateView(generics.CreateAPIView):
    """View for retrieving the Metadata Create."""

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()

# UpdateView


class MetadataUpdateView(generics.UpdateAPIView):
    """View for retrieving the Metadata Update."""

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()

# DeleteView


class MetadataDeleteView(generics.DestroyAPIView):
    """View for retrieving the Metadata Delete."""

    serializer_class = serializer.MetadataSerializer

    queryset = Metadata.objects.all()


# ContractMetadata

# ListView
class ContractMetadataListView(generics.ListAPIView):
    """View for retrieving the ContractMetadata List."""

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()

# OneView


class ContractMetadataOneView(generics.RetrieveAPIView):
    """View for retrieving the ContractMetadata entry."""

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()

# CreateView


class ContractMetadataCreateView(generics.CreateAPIView):
    """View for retrieving the ContractMetadata Create."""

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()

# UpdateView


class ContractMetadataUpdateView(generics.UpdateAPIView):
    """View for retrieving the ContractMetadata Update."""

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()

# DeleteView


class ContractMetadataDeleteView(generics.DestroyAPIView):
    """View for retrieving the ContractMetadata Delete."""

    serializer_class = serializer.ContractMetadataSerializer

    queryset = ContractMetadata.objects.all()



class CreateAdditionalMetaTagView(generics.CreateAPIView):
    """View for retrieving Create Additional Meta Tag."""

    serializer_class = serializer.MetadataSerializer

    def create(self, request, *args, **kwargs):
        metadata_serializer = self.get_serializer(data=request.data)
        metadata_serializer.is_valid(raise_exception=True)
        self.perform_create(metadata_serializer)
        headers = self.get_success_headers(metadata_serializer.data)
        return Response(metadata_serializer.data, status=201, headers=headers)


class AddAdditionalMetaTagToContractView(generics.CreateAPIView):
    """View for retrieving AddAdditional Meta Tag To Contract View."""

    serializer_class = serializer.ContractMetadataSerializer

    def create(self, request, *args, **kwargs):
        """View for retrieving with serializers View."""
        contract_metadata_serializer = self.get_serializer(data=request.data)
        contract_metadata_serializer.is_valid(raise_exception=True)
        self.perform_create(contract_metadata_serializer)
        headers = self.get_success_headers(contract_metadata_serializer.data)
        return Response(contract_metadata_serializer.data, status=201, headers=headers)

@api_view(['GET'])
def retrieve_all_additional_meta_tag(request, customer_id, contract_id):
    """Retrieve all additional meta tags for a specific contract."""
    try:
        contract_meta_tags = ContractMetadata.objects.filter(
            contract_id=contract_id)
        serialized_tags = []

        for tag in contract_meta_tags:
            serialized_tags.append({
                "additional_meta_tag_id": tag.additional_meta_tag_id,
                "additional_meta_tag": tag.metadata_value,
                "contract_id": tag.contract_id_id
            })

        return Response(serialized_tags, status=status.HTTP_200_OK)

    except ContractMetadata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


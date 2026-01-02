
from contract_renew import serializer
from contract_renew.models import RenewContract, UploadContract, UploadedContractStatus
from rest_framework import generics


# Create your views here.

# UploadContract

# ListView
class UploadContractListView(generics.ListAPIView):
    """View for retrieving the UploadContract List."""

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()

# OneView


class UploadContractOneView(generics.RetrieveAPIView):
    """View for retrieving the UploadContract entry."""

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()

# CreateView


class UploadContractCreateView(generics.CreateAPIView):
    """View for retrieving the UploadContract Create."""

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()

# UpdateView


class UploadContractUpdateView(generics.UpdateAPIView):
    """View for retrieving the UploadContract Update."""

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()

# DeleteView


class UploadContractDeleteView(generics.DestroyAPIView):
    """View for retrieving the UploadContract Delete."""

    serializer_class = serializer.UploadContractSerializer

    queryset = UploadContract.objects.all()

    #  RenewContract


# ListView
class RenewContractListView(generics.ListAPIView):
    """View for retrieving the RenewContract List."""

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()

# OneView


class RenewContractOneView(generics.RetrieveAPIView):
    """View for retrieving the RenewContract entry."""

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()

# CreateView


class RenewContractCreateView(generics.CreateAPIView):
    """View for retrieving the RenewContract Create."""

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()

# UpdateView


class RenewContractUpdateView(generics.UpdateAPIView):
    """View for retrieving the RenewContract Update."""

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()

# DeleteView


class RenewContractDeleteView(generics.DestroyAPIView):
    """View for retrieving the RenewContract Delete."""

    serializer_class = serializer.RenewContractSerializer

    queryset = RenewContract.objects.all()


# UploadedContractStatus

# ListView
class UploadedContractStatusListView(generics.ListAPIView):
    """View for retrieving the UploadedContractStatus List."""

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()

# OneView


class UploadedContractStatusOneView(generics.RetrieveAPIView):
    """View for retrieving the UploadedContractStatus entry."""

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()

# CreateView


class UploadedContractStatusCreateView(generics.CreateAPIView):
    """View for retrieving the UploadedContractStatus Create."""

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()

# UpdateView


class UploadedContractStatusUpdateView(generics.UpdateAPIView):
    """View for retrieving the UploadedContractStatus Update."""

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()

# DeleteView


class UploadedContractStatusDeleteView(generics.DestroyAPIView):
    """View for retrieving the UploadedContractStatus Delete."""

    serializer_class = serializer.UploadedContractStatusSerializer

    queryset = UploadedContractStatus.objects.all()

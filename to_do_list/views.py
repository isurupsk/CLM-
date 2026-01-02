from django.shortcuts import render
from rest_framework import generics
from to_do_list import serializer

from to_do_list.models import ActionItemList
# Create your views here.

################################################################
#######################   ActionItemList    ################
################################################################

# ListView
class ActionItemListListView(generics.ListAPIView):

    serializer_class = serializer.ActionItemListSerializer

    queryset = ActionItemList.objects.all()

# OneView
class ActionItemListOneView(generics.RetrieveAPIView):

    serializer_class = serializer.ActionItemListSerializer

    queryset = ActionItemList.objects.all()

# CreateView
class ActionItemListCreateView(generics.CreateAPIView):
    
    serializer_class = serializer.ActionItemListSerializer

    queryset = ActionItemList.objects.all()

# UpdateView
class ActionItemListUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.ActionItemListSerializer

    queryset = ActionItemList.objects.all()

# DeleteView
class ActionItemListDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.ActionItemListSerializer

    queryset = ActionItemList.objects.all()

###################### Janitha 06.30 ####################################
#Action Item List By Contract
class ActionItemListByContractView(generics.ListAPIView):
    """View for retrieving the tasks list for a given contract."""

    serializer_class = serializer.ActionItemListSerializer

    def get_queryset(self):
        contract_id = self.kwargs['contract_id']
        return ActionItemList.objects.filter(contract_id=contract_id)



class CompletedActionItemList(generics.ListAPIView):
    """View for retrieving the list of completed tasks."""

    serializer_class = serializer.ActionItemListSerializer

    def get_queryset(self):
        return ActionItemList.objects.filter(completed=True)


class ActionItemListToDoView(generics.ListAPIView):
    """View for retrieving the tasks to be done (not completed)."""

    serializer_class = serializer.ActionItemListSerializer

    def get_queryset(self):
        return ActionItemList.objects.filter(completed=False)
    
##################### End #################################################### 

######################## Janitha 07.06 #######################################

class RetrieveActionItemView(generics.RetrieveAPIView):
    serializer_class = serializer.ActionItemListSerializer
    queryset = ActionItemList.objects.all()
    lookup_field = 'action_item_id'

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        action_item_id = self.kwargs['action_item_id']
        return ActionItemList.objects.filter(customer_id=customer_id, action_item_id=action_item_id)


class RetrieveAllActionItemscontractView(generics.ListAPIView):
    serializer_class = serializer.ActionItemListSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        contract_id = self.kwargs['contract_id']
        return ActionItemList.objects.filter(customer_id=customer_id, contract_id=contract_id)

######################### End ################################################
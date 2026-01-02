from django.urls import path
from . import views

urlpatterns = [

    ################################################################
    ########################    ActionItemList    ##################
    ################################################################

    path('actionitemlist/create', views.ActionItemListCreateView.as_view(), name='actionitemlist_create'),
    path('actionitemlist/list', views.ActionItemListListView.as_view(), name='actionitemlist_list'),
    path('actionitemlist/retrieve/<int:pk>/', views.ActionItemListOneView.as_view(), name='actionitemlist_retrieve'),
    path('actionitemlist/update/<int:pk>/', views.ActionItemListUpdateView.as_view(), name='actionitemlist_update'),
    path('actionitemlist/delete/<int:pk>/', views.ActionItemListDeleteView.as_view(), name='actionitemlist_delete'),

    #################### Janitha 06.30 ####################################
    path('contract/<int:contract_id>/tasks/', views.ActionItemListByContractView.as_view(), name='contract-tasks'),

    path('tasks/completed/', views.CompletedActionItemList.as_view(), name='completed-tasks'),

    path('api/tasks/todo/', views.ActionItemListToDoView.as_view(), name='todo-tasks'),

    #################### End ###############################################

    ####################### Janitha 07.06 ######################################
    path('retrieve_action_item/<int:customer_id>/<int:action_item_id>/', 
         views.RetrieveActionItemView.as_view(), 
         name='retrieve_action_item'),

    path('retrieve_all_action_item_list/<int:customer_id>/<int:contract_id>/', 
         views.RetrieveAllActionItemscontractView.as_view(), 
         name='retrieve_all_action_item_list'),
    ###################### End ################################################


]
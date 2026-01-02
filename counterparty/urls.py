from django.urls import path
from . import views

urlpatterns = [

    # Counterparty

    path('Counterparty/create',
         views.CounterpartyCreateView.as_view(),
         name='Counterparty_create'),
    path('Counterparty/list',
         views.CounterpartyListView.as_view(),
         name='Counterparty_list'),
    path('Counterparty/retrieve/<int:pk>/',
         views.CounterpartyOneView.as_view(),
         name='Counterparty_retrieve'),
    path('Counterparty/update/<int:pk>/',
         views.CounterpartyUpdateView.as_view(),
         name='Counterparty_update'),
    path('Counterparty/delete/<int:pk>/',
         views.CounterpartyDeleteView.as_view(),
         name='Counterparty_delete'),
    path('counterparties_by_customer/<int:customer_id>/',
         views.CounterpartiesByCustomerView.as_view(),
         name='counterparties_by_customer'),

    # CustomerCounterpartyContact

    path('CustomerCounterpartyContact/create',
         views.CustomerCounterpartyContactCreateView.as_view(),
         name='CustomerCounterpartyContact_create'),
    path('CustomerCounterpartyContact/list',
         views.CustomerCounterpartyContactListView.as_view(),
         name='CustomerCounterpartyContact_list'),
    path('CustomerCounterpartyContact/retrieve/<int:pk>/',
         views.CustomerCounterpartyContactOneView.as_view(),
         name='CustomerCounterpartyContact_retrieve'),
    path('CustomerCounterpartyContact/update/<int:pk>/',
         views.CustomerCounterpartyContactUpdateView.as_view(),
         name='CustomerCounterpartyContact_update'),
    path('CustomerCounterpartyContact/delete/<int:pk>/',
         views.CustomerCounterpartyContactDeleteView.as_view(),
         name='CustomerCounterpartyContact_delete'),

    # CounterpartyContract

    path('CounterpartyContract/create',
         views.CounterpartyContractCreateView.as_view(),
         name='CounterpartyContract_create'),
    path('CounterpartyContract/list',
         views.CounterpartyContractListView.as_view(),
         name='CounterpartyContract_list'),
    path('CounterpartyContract/retrieve/<int:pk>/',
         views.CounterpartyContractOneView.as_view(),
         name='CounterpartyContract_retrieve'),
    path('CounterpartyContract/update/<int:pk>/',
         views.CounterpartyContractUpdateView.as_view(),
         name='CounterpartyContract_update'),
    path('CounterpartyContract/delete/<int:pk>/',
         views.CounterpartyContractDeleteView.as_view(),
         name='CounterpartyContract_delete'),
    ################# Janitha 07.06 #############################
    path('retrieve_all_counterparty_contact/<int:counterparty_id>/', 
         views.RetrieveAllCounterpartyContactView.as_view(), 
         name='retrieve_all_counterparty_contact'),
    ################ End ########################################





]

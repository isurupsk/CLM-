from django.urls import path
from . import views

urlpatterns = [

    # ContractTemplate

    path('contracttemplate/create',
         views.ContractTemplateCreateView.as_view(),
         name='contracttemplate_create'),
    path('contracttemplate/list',
         views.ContractTemplateListView.as_view(),
         name='contracttemplate_list'),
    path('contracttemplate/oneview/<int:pk>/',
         views.ContractTemplateOneView.as_view(),
         name='contracttemplate_oneview'),
    path('contracttemplate/update/<int:pk>/',
         views.ContractTemplateUpdateView.as_view(),
         name='contracttemplate_update'),
    path('contracttemplate/delete/<int:pk>/',
         views.ContractTemplateDeleteView.as_view(),
         name='contracttemplate_delete'),
    ############## Janitha 07.06 ##################
    path('retrieve_all_contract_template/<int:contract_type>/', 
         views.RetrieveAllContractTemplateView.as_view(), 
         name='retrieve_all_contract_template'),
    ############## End ############################

    # ContractType

    path('ContractType/create',
         views.ContractTypeCreateView.as_view(),
         name='ContractType_create'),
    path('ContractType/list',
         views.ContractTypeListView.as_view(),
         name='ContractType_list'),
    path('ContractType/oneview/<int:pk>/',
         views.ContractTypeOneView.as_view(),
         name='ContractType_oneview'),
    path('ContractType/update/<int:pk>/',
         views.ContractTypeUpdateView.as_view(),
         name='ContractType_update'),
    path('ContractType/delete/<int:pk>/',
         views.ContractTypeDeleteView.as_view(),
         name='ContractType_delete'),

    # ContractAttachment

    path('ContractAttachment/create',
         views.ContractAttachmentCreateView.as_view(),
         name='ContractAttachment_create'),
    path('ContractAttachment/list',
         views.ContractAttachmentListView.as_view(),
         name='ContractAttachment_list'),
    path('ContractAttachment/oneview/<int:pk>/',
         views.ContractAttachmentOneView.as_view(),
         name='ContractAttachment_oneview'),
    path('ContractAttachment/update/<int:pk>/',
         views.ContractAttachmentUpdateView.as_view(),
         name='ContractAttachment_update'),
    path('ContractAttachment/delete/<int:pk>/',
         views.ContractAttachmentDeleteView.as_view(),
         name='ContractAttachment_delete'),
    ################ Janitha 06.30 ########################################
    path('contracts/<int:contract_id>/attachments/', 
         views.ContractAttachmentByContractView.as_view(), 
         name='contract-attachments'),
    ################### End ###############################################  
    # Contract

    path('Contract/create',
         views.ContractCreateView.as_view(),
         name='Contract_create'),
    path('Contract/list',
         views.ContractListView.as_view(), name='Contract_list'),
    path('Contract/oneview/<int:pk>/',
         views.ContractOneView.as_view(),
         name='Contract_oneview'),
    path('Contract/update/<int:pk>/',
         views.ContractUpdateView.as_view(),
         name='Contract_update'),
    path('Contract/delete/<int:pk>/',
         views.ContractDeleteView.as_view(),
         name='Contract_delete'),

    path('Contract/by_status/<int:status_id>/',
         views.ContractsByStatusView.as_view(),
         name='contracts_by_status'),

    path('retrieve_all_contract_by_status/<int:customer_id>/<int:status_id>/',
         views.ContractsByStatusAndCustomerView.as_view(),
         name='retrieve_all_contract_by_status'),
    path('retrieve_all_contract/<int:customer_id>/',
         views.ContractsByCustomerView.as_view(),
         name='retrieve_all_contract'),
    path('contract_authors_by_contract/<int:contract_id>/',
         views.ContractAuthorsByContractView.as_view(),
         name='contract_authors_by_contract'),
    path('contract_versions_by_contract/<int:contract_id>/',
         views.ContractVersionsByContractView.as_view(),
         name='contract_versions_by_contract'),
    path('retrieve_contract_attachments/<int:contract_id>/',
         views.ContractAttachmentsByContractView.as_view(),
         name='retrieve_contract_attachments'),

    # ContractAuthor

    path('ContractAuthor/create',
         views.ContractAuthorCreateView.as_view(),
         name='ContractAuthor_create'),
    path('ContractAuthor/list',
         views.ContractAuthorListView.as_view(),
         name='ContractAuthor_list'),
    path('ContractAuthor/oneview/<int:pk>/',
         views.ContractAuthorOneView.as_view(),
         name='ContractAuthor_oneview'),
    path('ContractAuthor/update/<int:pk>/',
         views.ContractAuthorUpdateView.as_view(),
         name='ContractAuthor_update'),
    path('ContractAuthor/delete/<int:pk>/',
         views.ContractAuthorDeleteView.as_view(),
         name='ContractAuthor_delete'),

    # ContractCounterparty

    path('ContractCounterparty/create',
         views.ContractCounterpartyCreateView.as_view(),
         name='ContractCounterparty_create'),
    path('ContractCounterparty/list',
         views.ContractCounterpartyListView.as_view(),
         name='ContractCounterparty_list'),
    path('ContractCounterparty/oneview/<int:pk>/',
         views.ContractCounterpartyOneView.as_view(),
         name='ContractCounterparty_oneview'),
    path('ContractCounterparty/update/<int:pk>/',
         views.ContractCounterpartyUpdateView.as_view(),
         name='ContractCounterparty_update'),
    path('ContractCounterparty/delete/<int:pk>/',
         views.ContractCounterpartyDeleteView.as_view(),
         name='ContractCounterparty_delete'),

    # Country

    path('Country/create',
         views.CountryCreateView.as_view(), name='Country_create'),
    path('Country/list',
         views.CountryListView.as_view(), name='Country_list'),
    path('Country/oneview/<int:pk>/',
         views.CountryOneView.as_view(), name='Country_oneview'),
    path('Country/update/<int:pk>/',
         views.CountryUpdateView.as_view(), name='Country_update'),
    path('Country/delete/<int:pk>/',
         views.CountryDeleteView.as_view(), name='Country_delete'),

    #  ContractStatus

    path('ContractStatus/create',
         views.ContractStatusCreateView.as_view(),
         name='ContractStatus_create'),
    path('ContractStatus/list',
         views.ContractStatusListView.as_view(),
         name='ContractStatus_list'),
    path('ContractStatus/oneview/<int:pk>/',
         views.ContractStatusOneView.as_view(),
         name='ContractStatus_oneview'),
    path('ContractStatus/update/<int:pk>/',
         views.ContractStatusUpdateView.as_view(),
         name='ContractStatus_update'),
    path('ContractStatus/delete/<int:pk>/',
         views.ContractStatusDeleteView.as_view(),
         name='ContractStatus_delete'),

    # ContractHistory

    path('ContractHistory/create',
         views.ContractHistoryCreateView.as_view(),
         name='ContractHistory_create'),
    path('ContractHistory/list',
         views.ContractHistoryListView.as_view(),
         name='ContractHistory_list'),
    path('ContractHistory/oneview/<int:pk>/',
         views.ContractHistoryOneView.as_view(),
         name='ContractHistory_oneview'),
    path('ContractHistory/update/<int:pk>/',
         views.ContractHistoryUpdateView.as_view(),
         name='ContractHistory_update'),
    path('ContractHistory/delete/<int:pk>/',
         views.ContractHistoryDeleteView.as_view(),
         name='ContractHistory_delete'),

    ############## Janitha 07.06 ######################
    path('retrieve_all_contract_history/<int:contract_id>/', 
         views.RetrieveAllContractHistoryView.as_view(), 
         name='retrieve_all_contract_history'),
    ############## End ################################
]

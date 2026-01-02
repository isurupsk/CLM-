from django.urls import path
from . import views

urlpatterns = [


    # ContractReviewer

    path('ContractReviewer/create',
         views.ContractReviewerCreateView.as_view(),
         name='ContractReviewer_create'),
    path('ContractReviewer/list',
         views.ContractReviewerListView.as_view(),
         name='ContractReviewer_list'),
    path('ContractReviewer/retrieve/<int:pk>/',
         views.ContractReviewerOneView.as_view(),
         name='ContractReviewer_retrieve'),
    path('ContractReviewer/update/<int:pk>/',
         views.ContractReviewerUpdateView.as_view(),
         name='ContractReviewer_update'),
    path('ContractReviewer/delete/<int:pk>/',
         views.ContractReviewerDeleteView.as_view(),
         name='ContractReviewer_delete'),
    path('retrieve_all_contract_reviewer/<int:contract_id>/',
         views.ContractReviewersByContractView.as_view(),
         name='retrieve_all_contract_reviewer'),
    ################## Anura 30/06/2023 #################
     path('ContractReviewer/retrieve/completed/',
         views.ContractRevieverCompletedView.as_view(),
         name='ContractReviever_completed_retrieve'),
     path('ContractReviewer/retrieve/current/',
         views.ContractRevieverCurrentView.as_view(),
         name='ContractReviever_completed_retrieve'),
     ####################### End ##########################
     
     ###################### Janitha 07.06 #################
     path('retrieve_all_contract_reviewer/<int:contract_id>/', 
          views.RetrieveAllContractReviewerView.as_view(), 
          name='retrieve_all_contract_reviewer'),
     ##################### End ############################

    # ContractActivityLog

    path('ContractActivityLog/create',
         views.ContractActivityLogCreateView.as_view(),
         name='ContractActivityLog_create'),
    path('ContractActivityLog/list',
         views.ContractActivityLogListView.as_view(),
         name='ContractActivityLog_list'),
    path('ContractActivityLog/retrieve/<int:pk>/',
         views.ContractActivityLogOneView.as_view(),
         name='ContractActivityLog_retrieve'),
    path('ContractActivityLog/update/<int:pk>/',
         views.ContractActivityLogUpdateView.as_view(),
         name='ContractActivityLog_update'),
    path('ContractActivityLog/delete/<int:pk>/',
         views.ContractActivityLogDeleteView.as_view(),
         name='ContractActivityLog_delete'),

    # ContractApprover

    path('ContractApprover/create',
         views.ContractApproverCreateView.as_view(),
         name='ContractApprover_create'),
    path('ContractApprover/list',
         views.ContractApproverListView.as_view(),
         name='ContractApprover_list'),
    path('ContractApprover/retrieve/<int:pk>/',
         views.ContractApproverOneView.as_view(),
         name='ContractApprover_retrieve'),
    path('ContractApprover/update/<int:pk>/',
         views.ContractApproverUpdateView.as_view(),
         name='ContractApprover_update'),
    path('ContractApprover/delete/<int:pk>/',
         views.ContractApproverDeleteView.as_view(),
         name='ContractApprover_delete'),
    path('retrieve_all_contract_approvers/<int:contract_id>/',
         views.ContractApproversByContractView.as_view(),
         name='retrieve_all_contract_approvers'),
     ################## Anura 30/06/2023 #################
     path('ContractApprover/retrieve/completed/',
         views.ContractApproverCompletedView.as_view(),
         name='ContractApprover_completed_retrieve'),
     path('ContractApprover/retrieve/current/',
         views.ContractApproverCurrentView.as_view(),
         name='ContractApprover_completed_retrieve'),
     ####################### End ##########################

    # Metadata

    path('Metadata/create',
         views.MetadataCreateView.as_view(),
         name='Metadata_create'),
    path('Metadata/list',
         views.MetadataListView.as_view(),
         name='Metadata_list'),
    path('Metadata/retrieve/<int:pk>/',
         views.MetadataOneView.as_view(),
         name='Metadata_retrieve'),
    path('Metadata/update/<int:pk>/',
         views.MetadataUpdateView.as_view(),
         name='Metadata_update'),
    path('Metadata/delete/<int:pk>/',
         views.MetadataDeleteView.as_view(),
         name='Metadata_delete'),

    path('create_additional_meta_tag/',
         views.CreateAdditionalMetaTagView.as_view(),
         name='create_additional_meta_tag'),
    path('add_additional_meta_tag_to_contract/',
         views.AddAdditionalMetaTagToContractView.as_view(),
         name='add_additional_meta_tag_to_contract'),

    # ContractMetadata

    path('ContractMetadata/create',
         views.ContractMetadataCreateView.as_view(),
         name='ContractMetadata_create'),
    path('ContractMetadata/list',
         views.ContractMetadataListView.as_view(),
         name='ContractMetadata_list'),
    path('ContractMetadata/retrieve/<int:pk>/',
         views.ContractMetadataOneView.as_view(),
         name='ContractMetadata_retrieve'),
    path('ContractMetadata/update/<int:pk>/',
         views.ContractMetadataUpdateView.as_view(),
         name='ContractMetadata_update'),
    path('ContractMetadata/delete/<int:pk>/',
         views.ContractMetadataDeleteView.as_view(),
         name='ContractMetadata_delete'),

    path('retrieve_all_additional_meta_tag/<int:customer_id>/<int:contract_id>/',
         views.retrieve_all_additional_meta_tag,
         name='retrieve_all_additional_meta_tag'),



]

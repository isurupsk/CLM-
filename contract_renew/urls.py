from django.urls import path
from . import views

urlpatterns = [

    # UploadContract

    path('UploadContract/create',
         views.UploadContractCreateView.as_view(),
         name='UploadContract_create'),
    path('UploadContract/list',
         views.UploadContractListView.as_view(),
         name='UploadContract_list'),
    path('UploadContract/retrieve/<int:pk>/',
         views.UploadContractOneView.as_view(),
         name='UploadContract_retrieve'),
    path('UploadContract/update/<int:pk>/',
         views.UploadContractUpdateView.as_view(),
         name='UploadContract_update'),
    path('UploadContract/delete/<int:pk>/',
         views.UploadContractDeleteView.as_view(),
         name='UploadContract_delete'),

    # RenewContract

    path('RenewContract/create',
         views.RenewContractCreateView.as_view(),
         name='RenewContract_create'),
    path('RenewContract/list',
         views.RenewContractListView.as_view(),
         name='RenewContract_list'),
    path('RenewContract/retrieve/<int:pk>/',
         views.RenewContractOneView.as_view(),
         name='RenewContract_retrieve'),
    path('RenewContract/update/<int:pk>/',
         views.RenewContractUpdateView.as_view(),
         name='RenewContract_update'),
    path('RenewContract/delete/<int:pk>/',
         views.RenewContractDeleteView.as_view(),
         name='RenewContract_delete'),

    # UploadedContractStatus

    path('UploadedContractStatus/create',
         views.UploadedContractStatusCreateView.as_view(),
         name='UploadedContractStatus_create'),
    path('UploadedContractStatus/list',
         views.UploadedContractStatusListView.as_view(),
         name='UploadedContractStatus_list'),
    path('UploadedContractStatus/retrieve/<int:pk>/',
         views.UploadedContractStatusOneView.as_view(),
         name='UploadedContractStatus_retrieve'),
    path('UploadedContractStatus/update/<int:pk>/',
         views.UploadedContractStatusUpdateView.as_view(),
         name='UploadedContractStatus_update'),
    path('UploadedContractStatus/delete/<int:pk>/',
         views.UploadedContractStatusDeleteView.as_view(),
         name='UploadedContractStatus_delete'),


]

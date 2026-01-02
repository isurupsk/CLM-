from django.urls import path
from . import views

####################### Anura 21/06/2023 ##########################
urlpatterns = [

    # labelsByCustomer
    path('labels_by_customer/<int:customer_id>/',
         views.LabelsByCustomerView.as_view(),
         name='labels_by_customer'),
    ################## Janitha 06.30 ###################################

    path('contracts/<int:contract_id>/labels/', 
         views.ContractLabelByContractView.as_view(), 
         name='contract-labels'),

    ################## End #############################################
]
############################# End ##################################


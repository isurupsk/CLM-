from django.urls import path
from . import views

urlpatterns = [

    ################################################################
    ########################    Language    ########################
    ################################################################

    path('language/create', views.LanguageCreateView.as_view(), name='language_create'),
    path('language/list', views.LanguageListView.as_view(), name='language_list'),
    path('language/retrieve/<int:pk>/', views.LanguageOneView.as_view(), name='language_retrieve'),
    path('language/update/<int:pk>/', views.LanguageUpdateView.as_view(), name='language_update'),
    path('language/delete/<int:pk>/', views.LanguageDeleteView.as_view(), name='language_delete'),
    ###################### Janitha 07.07 ##################################
    path('retrieve_all_languages/<int:customer_id>/', views.RetrieveAllLanguagesView.as_view(), name='retrieve_all_languages'),
    ##################### End ############################################

    ################################################################
    ########################    Currency    ########################
    ################################################################

    path('currency/create', views.CurrencyCreateView.as_view(), name='currency_create'),
    path('currency/list', views.CurrencyListView.as_view(), name='currency_list'),
    path('currency/retrieve/<int:pk>/', views.CurrencyOneView.as_view(), name='currency_retrieve'),
    path('currency/update/<int:pk>/', views.CurrencyUpdateView.as_view(), name='currency_update'),
    path('currency/delete/<int:pk>/', views.CurrencyDeleteView.as_view(), name='currency_delete'),
    ################################# Janitha 07.07 ######################################
    path('retrieve_all_currencies/<int:customer_id>/', views.RetrieveAllCurrenciesView.as_view(), name='retrieve_all_currencies'),
    ################################# End ###############################################

    ################################################################
    ########################    DateFormat    ######################
    ################################################################

    path('dateformat/create', views.DateFormatCreateView.as_view(), name='dateformat_create'),
    path('dateformat/list', views.DateFormatListView.as_view(), name='dateformat_list'),
    path('dateformat/retrieve/<int:pk>/', views.DateFormatOneView.as_view(), name='dateformat_retrieve'),
    path('dateformat/update/<int:pk>/', views.DateFormatUpdateView.as_view(), name='dateformat_update'),
    path('dateformat/delete/<int:pk>/', views.DateFormatDeleteView.as_view(), name='dateformat_delete'),
    ################################# Janitha 07.07 ######################################
    path('retrieve_all_date_formats/<int:customer_id>/', views.RetrieveAllDateFormatsView.as_view(), name='retrieve_all_date_formats'),
    ################################# End ###############################################




]
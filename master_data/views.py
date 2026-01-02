from django.shortcuts import render

from rest_framework import generics

from master_data import serializer
from master_data.models import Currency, DateFormat, Language
# Create your views here.


################################################################
#######################   Language    ##########################
################################################################

# ListView
class LanguageListView(generics.ListAPIView):

    serializer_class = serializer.LanguageSerializer

    queryset = Language.objects.all()

# OneView
class LanguageOneView(generics.RetrieveAPIView):

    serializer_class = serializer.LanguageSerializer

    queryset = Language.objects.all()

# CreateView
class LanguageCreateView(generics.CreateAPIView):
    
    serializer_class = serializer.LanguageSerializer

    queryset = Language.objects.all()

# UpdateView
class LanguageUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.LanguageSerializer

    queryset = Language.objects.all()

# DeleteView
class LanguageDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.LanguageSerializer

    queryset = Language.objects.all()

################## Janitha 07.07 ########################

class RetrieveAllLanguagesView(generics.ListAPIView):
    serializer_class = serializer.LanguageSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Language.objects.filter(customer_id=customer_id)

################## End ####################################


################################################################
#######################   Currency    ##########################
################################################################

# ListView
class CurrencyListView(generics.ListAPIView):

    serializer_class = serializer.CurrencySerializer

    queryset = Currency.objects.all()

# OneView
class CurrencyOneView(generics.RetrieveAPIView):

    serializer_class = serializer.CurrencySerializer

    queryset = Currency.objects.all()

# CreateView
class CurrencyCreateView(generics.CreateAPIView):
    
    serializer_class = serializer.CurrencySerializer

    queryset = Currency.objects.all()

# UpdateView
class CurrencyUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.CurrencySerializer

    queryset = Currency.objects.all()

# DeleteView
class CurrencyDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.CurrencySerializer

    queryset = Currency.objects.all()

######################### Janitha 07.07 #########################

class RetrieveAllCurrenciesView(generics.ListAPIView):
    serializer_class = serializer.CurrencySerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Currency.objects.filter(customer_id=customer_id)

########################### End ################################


################################################################
#######################   DateFormate    #######################
################################################################

# ListView
class DateFormatListView(generics.ListAPIView):

    serializer_class = serializer.DateFormatSerializer

    queryset = DateFormat.objects.all()

# OneView
class DateFormatOneView(generics.RetrieveAPIView):

    serializer_class = serializer.DateFormatSerializer

    queryset = DateFormat.objects.all()

# CreateView
class DateFormatCreateView(generics.CreateAPIView):
    
    serializer_class = serializer.DateFormatSerializer

    queryset = DateFormat.objects.all()

# UpdateView
class DateFormatUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.DateFormatSerializer

    queryset = DateFormat.objects.all()

# DeleteView
class DateFormatDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.DateFormatSerializer

    queryset = DateFormat.objects.all()

############################### Janitha 07.07 #######################

class RetrieveAllDateFormatsView(generics.ListAPIView):
    serializer_class = serializer.DateFormatSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return DateFormat.objects.filter(customer_id=customer_id)

############################### End #################################
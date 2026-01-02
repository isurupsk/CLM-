from django import forms
from django.contrib import admin
from contract.models import CountryContract

from to_do_list.serializer import ActionItemListSerializer

# Register your models here.
from .models import ActionItemList

admin.site.register(ActionItemList)

class ActionItemListForm(forms.ModelForm):
    class Meta:
        model = ActionItemList
        fields = '__all__'

class ActionItemListAdmin(admin.ModelAdmin):
    form = ActionItemListSerializer
 


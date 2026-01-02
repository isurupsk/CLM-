from django.contrib import admin

# Register your models here.


from .models import LabelMaster, ContractLabel, ContractFolder

admin.site.register(LabelMaster)
admin.site.register(ContractLabel)
admin.site.register(ContractFolder)


from django.contrib import admin

# Register your models here.


from .models import UploadContract, RenewContract, UploadedContractStatus

admin.site.register(UploadContract)
admin.site.register(RenewContract)
admin.site.register(UploadedContractStatus)

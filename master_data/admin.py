from django.contrib import admin

# Register your models here.


from .models import Language, Currency, DateFormat


admin.site.register(Language)
admin.site.register(Currency)
admin.site.register(DateFormat)

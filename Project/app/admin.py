from django.contrib import admin
from .models import AdminDataBase ,UserDataBase ,EnquiryDataBase
# Register your models here.
admin.site.register(AdminDataBase)
admin.site.register(UserDataBase)
admin.site.register(EnquiryDataBase)


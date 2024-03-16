from django.contrib import admin
from .models import(
    UserInfo, CustInfo
)
# Register your models here.

admin.site.register(
    [UserInfo, CustInfo]
)
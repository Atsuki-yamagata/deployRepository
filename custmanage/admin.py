from django.contrib import admin
from .models import( CustInfo )
from accounts.models import Users

# Register your models here.

admin.site.register(
    [Users, CustInfo]
)
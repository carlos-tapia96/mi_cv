from django.contrib import admin
from . models import (
    Portfolio
)

# Register your models here.
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)
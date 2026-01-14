from django.contrib import admin
from .models import Fee

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):  
    list_display = ('id', 'amount', 'due_date', 'category')
    search_fields = ('category__name',)
    list_filter = ('due_date',)
from django.contrib import admin
<<<<<<< HEAD
from .models import Fee
=======
from .models import Fee, FeeCategory
>>>>>>> 2bc03f151455db2cd1293f71eb0da35d96c394f6

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):  
    list_display = ('id', 'amount', 'due_date', 'category')
    search_fields = ('category__name',)
    list_filter = ('due_date',)
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_code',
        'first_name',
        'last_name',
        'grade',
        'status',
        'guardian_phone',
    )

    list_filter = ('status', 'grade')
    search_fields = ('student_code', 'first_name', 'last_name', 'guardian_phone')

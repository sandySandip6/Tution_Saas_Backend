from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'schedule')
    search_fields = ('name',)
    list_filter = ('schedule',)

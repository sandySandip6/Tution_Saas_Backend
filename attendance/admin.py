from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'date', 'status')
    search_fields = ('student__first_name', 'student__last_name')
<<<<<<< HEAD
    list_filter = ('date', 'status')


=======
    list_filter = ('date', 'status')
>>>>>>> 2bc03f151455db2cd1293f71eb0da35d96c394f6

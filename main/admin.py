from django.contrib import admin
from .models import *

admin.site.register(StudentClassInfo)


@admin.register(StudentInfo)
class StudentInfo(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'class_type', 'gender', 'section', 'shift_name', 'admission_date',
                    'academic_year', 'guardian_name', 'guardian_email', 'emergency_phone',
                    'created_by', 'updated_by'
                    ]
    search_fields = ['name', 'section']
    ordering = ['id']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'status']
    search_fields = ['student', 'date']


admin.site.register(Attendance, AttendanceAdmin)

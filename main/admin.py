from django.contrib import admin
from .models import *

# Registering StudentClassInfo model with the admin site
admin.site.register(StudentClassInfo)

# Customizing the admin interface for StudentInfo model
@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    """
    Customized admin interface for StudentInfo model.
    """
    list_display = ['id', 'name', 'age', 'class_type', 'gender', 'section', 'shift_name', 'admission_date',
                    'academic_year', 'guardian_name', 'guardian_email', 'emergency_phone',
                    'created_by', 'updated_by'
                    ]
    search_fields = ['name', 'section']
    ordering = ['id']

# Customizing the admin interface for Attendance model
class AttendanceAdmin(admin.ModelAdmin):
    """
    Customized admin interface for Attendance model.
    """
    list_display = ['student', 'date', 'status']
    search_fields = ['student', 'date']

# Registering Attendance model with the customized admin interface
admin.site.register(Attendance, AttendanceAdmin)

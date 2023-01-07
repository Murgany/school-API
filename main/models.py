from django.db import models
from django.conf import settings
from django.contrib.admin import autodiscover


class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=30, help_text='Senior one')
    class_short_form = models.CharField(max_length=10, help_text='S1')

    def __str__(self):
        return self.class_name


class StudentInfo(models.Model):
    academic_year = models.CharField(max_length=20)
    admission_date = models.DateField()
    name = models.CharField(max_length=100, help_text='John Doe')
    age = models.IntegerField()
    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(choices=gender_choice, max_length=20)
    class_type = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    shift_name = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100, help_text='John Doe')
    emergency_phone = models.IntegerField(unique=True, null=True)
    guardian_email = models.EmailField(max_length=30, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, related_name='create')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, related_name='update')
    
    class Meta:
        unique_together = ['id', 'name']
    
    def __str__(self):
        return self.name

        
class AttendanceManager(models.Manager):
    def create_attendance(self, name):
        student_obj = StudentInfo.objects.get(
            class_name__class_short_form=name,
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status='status')
        return attendance_obj


class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status_choice = (
        ('P', 'Present'),
        ('A', 'Absent')
    )
    status = models.CharField(choices=status_choice, max_length=15, default='Present')

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

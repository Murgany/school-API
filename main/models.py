from django.db import models
from django.conf import settings
from django.contrib.admin import autodiscover


class StudentClassInfo(models.Model):
"""
StudentClassInfo

    class_name: CharField, max length 30. Represents the name of the class (e.g., "Senior one").
    class_short_form: CharField, max length 10. Represents a shortened form of the class name (e.g., "S1").
"""

    class_name = models.CharField(max_length=30, help_text='Senior one')
    class_short_form = models.CharField(max_length=10, help_text='S1')

    def __str__(self):
        return self.class_name


class StudentInfo(models.Model):
    """
    StudentInfo

    academic_year: CharField, max length 20. Represents the academic year of the student.
    admission_date: DateField. Represents the date of admission.
    name: CharField, max length 100. Represents the name of the student.
    age: IntegerField. Represents the age of the student.
    gender: CharField with choices (M, F, O) representing gender (Male, Female, Other).
    class_type: ForeignKey to StudentClassInfo, representing the class the student belongs to.
    section: CharField, max length 100. Represents the section the student belongs to.
    shift_name: CharField, max length 100. Represents the shift the student is part of.
    guardian_name: CharField, max length 100. Represents the name of the guardian.
    emergency_phone: IntegerField, unique. Represents the emergency contact phone number.
    guardian_email: EmailField, max length 30. Represents the email of the guardian.
    created_by: ForeignKey to the user model, representing the user who created the record.
    updated_by: ForeignKey to the user model, representing the user who last updated the record.

    
    The unique_together constraints in Meta ensure uniqueness based on certain fields in the database. 
    In StudentInfo, it ensures uniqueness based on both id and name. 
    """
    
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
    """
    AttendanceManager

     A custom manager for the Attendance model providing a method:
     create_attendance(name): Creates an attendance record for a student based on the provided name.
    """
    
    def create_attendance(self, name):
        student_obj = StudentInfo.objects.get(
            class_name__class_short_form=name,
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status='status')
        return attendance_obj


class Attendance(models.Model):
    """
    Attendance

    student: ForeignKey to StudentInfo, representing the student whose attendance is being recorded.
    date: DateField with auto_now_add=True, representing the date of the attendance record.
    status: CharField with choices (P, A) representing attendance status (Present, Absent).

    The unique_together constraints in Meta ensure uniqueness based on certain fields in the database. In StudentInfo, 
    it ensures uniqueness based on both id and name. In Attendance, it ensures uniqueness based on both student and date.Attendance

    student: ForeignKey to StudentInfo, representing the student whose attendance is being recorded.
    date: DateField with auto_now_add=True, representing the date of the attendance record.
    status: CharField with choices (P, A) representing attendance status (Present, Absent).

    The unique_together constraints in Meta ensure uniqueness based on certain fields in the database. 
    In Attendance, it ensures uniqueness based on both student and date.
    """
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

from rest_framework import serializers
from .models import StudentInfo, StudentClassInfo, Attendance
from django.contrib.auth.models import User, Group
from django import forms

class StudentInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for StudentInfo model.
    """
    # Customizing admission_date field widget
    admission_date = forms.DateField(widget=forms.DateInput(format='%m/%d%Y'))

    class Meta:
        model = StudentInfo
        fields = ['id', 'name', 'age', 'class_type', 'gender', 'section', 'shift_name', 'admission_date', 'academic_year', 
                  'guardian_name', 'guardian_email', 'emergency_phone','created_by', 'updated_by'
                  ]


class StudentClassInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for StudentClassInfo model.
    """
    class Meta:
        model = StudentClassInfo
        fields = ['class_name', 'class_short_form', 'class_count']


class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer for Attendance model.
    """
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user.
        """
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for Group model.
    """
    class Meta:
        model = Group
        fields = ["name"]

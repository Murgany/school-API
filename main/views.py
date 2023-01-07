from .serializers import *
from .models import StudentInfo, StudentClassInfo
from rest_framework import status
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework import viewsets


# CRUD Views for all models bellow. All are self-explanatory

class StudentInfoViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        students = StudentInfo.objects.all()
        serializer = StudentInfoSerializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = StudentInfo.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentInfoSerializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        student = StudentInfo.objects.get(pk=pk)
        serializer = StudentInfoSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student = StudentInfo.objects.get(pk=pk)
        serializer = StudentInfoSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user)
            return Response({'http_method': 'PATCH'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = StudentInfo.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentClassInfoViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        students = StudentClassInfo.objects.all()
        serializer = StudentClassInfoSerializer(students, many=True)
        ordering = ["-id"]
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentClassInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = StudentClassInfo.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentClassInfoSerializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        student = StudentClassInfo.objects.get(pk=pk)
        serializer = StudentClassInfoSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = StudentClassInfo.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttendanceViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        students = Attendance.objects.all()
        serializer = AttendanceSerializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Attendance.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = AttendanceSerializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        student = Attendance.objects.get(pk=pk)
        serializer = AttendanceSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student = Attendance.objects.get(pk=pk)
        serializer = AttendanceSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=self.request.user)
            return Response({'http_method': 'PATCH'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = Attendance.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# User registration view

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

    def get_post_response_data(self, request, token, instance):
        # serializer = self.get_user_serializer_class()
        # staff_perms = self.request.user.get_user_permissions()
        user_group = Group.objects.get(user=request.user).name
        data = {
            'username': request.user.username,
            'token': token,
            'expiry': self.format_expiry_datetime(instance.expiry),
            "user_group": user_group,
        }
        return data

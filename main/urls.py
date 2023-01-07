from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from knox.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter(trailing_slash=False)
router.register('student_info/?', StudentInfoViewSet, basename='student_info'),
router.register('class_info', StudentClassInfoViewSet, basename='class_info'),
router.register('attendance', AttendanceViewSet, basename='attendance'),

urlpatterns = [
    path('', include(router.urls)),
    path('api/register', RegisterAPI.as_view(), name='register'),
    path('api/login', LoginView.as_view()),
    path('api/logout', LogoutView.as_view(), name='knox_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

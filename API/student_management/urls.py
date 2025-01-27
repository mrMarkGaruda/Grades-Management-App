from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, SubjectViewSet, GradeViewSet

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('subjects', SubjectViewSet)
router.register('grades', GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
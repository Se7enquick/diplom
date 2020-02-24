from .viewsets import TaskViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

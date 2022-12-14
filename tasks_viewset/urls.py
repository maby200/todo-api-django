from rest_framework.routers import DefaultRouter
from .views import TasksViewSet, TaskReadOnlyViewSet

tasks_router = DefaultRouter()

tasks_router.register(r'v2/todo', TasksViewSet, basename='todo_model_viewset')
tasks_router.register(r'v3/todo', TaskReadOnlyViewSet, basename='todo_read_only')

urlpatterns = tasks_router.urls
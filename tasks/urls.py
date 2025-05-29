from django.urls import path

from .views import RiskyTaskView, TaskEnqueueView

urlpatterns = [
    path("enqueue/", TaskEnqueueView.as_view(), name="enqueue_task"),
    path("risky/", RiskyTaskView.as_view(), name="risky_task"),
]

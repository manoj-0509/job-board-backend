from django.urls import path
from .views import get_jobs, get_job

urlpatterns = [
    path('jobs/', get_jobs),
    path('job/<int:job_id>/', get_job),
]

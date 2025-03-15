# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Job
from .serializers import JobSerializer

@api_view(['GET'])
def get_jobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_job(request, job_id):
    job = Job.objects.get(id=job_id)
    serializer = JobSerializer(job)
    return Response(serializer.data)

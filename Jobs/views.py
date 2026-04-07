from django.shortcuts import render

from Jobs.api.permissions import EditJobs, PostJobs
from .models import Job
from .api.serializers import JobSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

class JobViewSet(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [PostJobs]
    
    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
    
class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [EditJobs]
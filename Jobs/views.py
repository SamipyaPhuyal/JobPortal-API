from django.shortcuts import render

from Jobs.api.permissions import ApplyJobs, EditJobs, PostJobs
from .models import Application, Job
from .api.serializers import ApplicationSerializer, JobSerializer
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

class ApplicationView(APIView):
    serializer_class = ApplicationSerializer
    permission_classes = [ApplyJobs]
    def post(self, request,pk):
        job = Job.objects.get(pk=pk)
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(applicant=request.user, job=job)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
       
    def delete(self, request, pk):
        application = Application.objects.get(pk=pk, applicant=request.user)
        application.delete()
        return Response("message: Application withdrawn", status=204)
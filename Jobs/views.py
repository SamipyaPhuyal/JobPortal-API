from django.shortcuts import redirect, render

from Jobs.api.permissions import ApplyJobs, EditJobs, PostJobs
from .models import Application, Job
from .api.serializers import ApplicationSerializer, JobSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from Jobs.api.pagination import JobPagination

class JobViewSet(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [PostJobs]
    pagination_class = JobPagination
    
    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
    
class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [EditJobs]

class ApplicationView(APIView):
    serializer_class = ApplicationSerializer
    permission_classes = [ApplyJobs]
    
    def get(self, request, pk=None):
        if pk:
            try:
                application = Application.objects.get(pk=pk, applicant=request.user)
            except Application.DoesNotExist:
                application = Application.objects.get(pk=pk, job__posted_by=request.user)

            serializer = ApplicationSerializer(application)
            return Response(serializer.data)
        elif request.user.is_authenticated:
            applications = Application.objects.filter(applicant=request.user)
            serializer = ApplicationSerializer(applications, many=True)
            return Response(serializer.data)
    def post(self, request,pk):
        job = Job.objects.get(pk=pk)
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(applicant=request.user, job=job)
            job.update(total_applications=job.total_applications + 1)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
       
    def delete(self, request, pk):
        application = Application.objects.get(pk=pk, applicant=request.user)
        application.delete()
        return Response({"message": "Application withdrawn"}, status=204)
    
    def patch(self, request, pk):
        application=Application.objects.get(pk=pk)
        if (application.applicant == (request.user) or application.job.posted_by == (request.user)) or request.user.is_staff:
            serializer = ApplicationSerializer(application, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response({"message": "You do not have permission to update this application."}, status=403)

class ApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    
    def get_queryset(self):
        user = self.request.user
        user_type=getattr(getattr(user, 'userprofile', None), 'type', None)
        if user_type == "employee":
            return Application.objects.filter(applicant=user)
        elif user_type == "employer":
            return Application.objects.filter(job__posted_by=user)
        return redirect('job-list')
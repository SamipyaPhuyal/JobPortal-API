from urllib import request

from Jobs.models import Application, Job
from rest_framework import serializers  

class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.SerializerMethodField()
    class Meta:
        model = Job
        fields ="__all__"
        read_only_fields = ["posted_by","total_applications"]
    def get_posted_by(self, obj):
        return obj.posted_by.username
    
class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField(read_only=True)
    job = serializers.CharField(source="job.position", read_only=True)
    class Meta:
        model = Application
        fields ="__all__"
        read_only_fields = ["applicant", "job","cover_letter","status"]
    def get_job(self, obj):
        return obj.job.position
   
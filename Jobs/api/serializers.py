from urllib import request

from Jobs.models import Job
from rest_framework import serializers  

class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.SerializerMethodField()
    class Meta:
        model = Job
        fields ="__all__"
        read_only_fields = ["posted_by"]
    def get_posted_by(self, obj):
        return obj.posted_by.username
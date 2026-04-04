from Jobs.models import Job
from rest_framework import serializers  

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields =['id', 'position', 'company', 'location', 'type']
        
class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields =['id', 'position', 'company', 'location', 'description', 'requirements', 'type']
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100) 
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    type = models.CharField(max_length=50)
    posted_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    def __str__(self):
        return self.position
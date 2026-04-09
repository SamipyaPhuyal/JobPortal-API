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
    posted_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_by')
    def __str__(self):
        return self.position
    
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applicant')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Reviewing')
    
    def __str__(self):
        return f"{self.applicant.username} - {self.job.position}"
from django.contrib import admin

from Jobs.models import Application, Job

# Register your models here.
admin.site.register(Job)
admin.site.register(Application)
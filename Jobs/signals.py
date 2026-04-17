from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache
from .models import Job, Application


@receiver([post_save,post_delete],sender=Job)
def invalidate_cache(sender,instance, **kwargs):
    cache.delete_pattern('*job-list*')
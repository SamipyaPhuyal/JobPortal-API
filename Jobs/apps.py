from django.apps import AppConfig


class JobsConfig(AppConfig):
    name = 'Jobs'
    
    def ready(self):
        from . import signals

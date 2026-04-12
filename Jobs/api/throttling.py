from rest_framework.throttling import SimpleRateThrottle,UserRateThrottle

class ListRateThrottle(SimpleRateThrottle):
    scope = 'job-list'


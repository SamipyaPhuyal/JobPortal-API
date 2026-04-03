from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class LoginThrottle(UserRateThrottle):
    scope = 'login_attempts'
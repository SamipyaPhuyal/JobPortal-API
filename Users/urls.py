from django.contrib import admin
from django.urls import path
from Users.views import RegistrationView, UserProfileView, UserViewSet
from Users.views import RegistrationView,LogoutView , UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('list/', UserViewSet.as_view(), name='users-list-create'),
    path('profile/', UserProfileView.as_view(), name='users-profile'),
    path('register/', RegistrationView.as_view(), name='users-register'),
    path('login/', TokenObtainPairView.as_view(), name='users-login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='users-logout'),
]

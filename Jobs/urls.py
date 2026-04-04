
from django.urls import include, path
from Jobs.views import JobDetailView, JobViewSet


urlpatterns = [
    path('list/', JobViewSet.as_view(), name='job-list'),
    path('detail/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
]

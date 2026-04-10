
from django.urls import include, path
from Jobs.views import ApplicationListView, ApplicationView, JobDetailView, JobViewSet


urlpatterns = [
    path('list/', JobViewSet.as_view(), name='job-list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path("<int:pk>/apply/", ApplicationView.as_view(), name="job-apply"),
    path("applications/", ApplicationListView.as_view(), name="job-applications"),
    path("application/<int:pk>/", ApplicationView.as_view(), name="application-detail"),
]

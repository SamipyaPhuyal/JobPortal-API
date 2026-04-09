
from django.urls import include, path
from Jobs.views import ApplicationView, JobDetailView, JobViewSet


urlpatterns = [
    path('list/', JobViewSet.as_view(), name='job-list'),
    path('detail/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path("detail/<int:pk>/apply/", ApplicationView.as_view(), name="job-apply"),
    path("application/<int:pk>/withdraw/", ApplicationView.as_view(), name="application-withdraw"),
]

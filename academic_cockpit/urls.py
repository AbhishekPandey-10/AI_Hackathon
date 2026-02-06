from django.urls import path
from .views import AcademicDashboardView

app_name = 'academic_cockpit'

urlpatterns = [
    path('schedule/', AcademicDashboardView.as_view(), name='schedule'),
]

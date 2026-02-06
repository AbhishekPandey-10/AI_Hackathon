from django.urls import path
from .views import ComplaintListView, ComplaintCreateView

app_name = 'administration'

urlpatterns = [
    path('complaints/', ComplaintListView.as_view(), name='complaint_list'),
    path('complaints/new/', ComplaintCreateView.as_view(), name='complaint_create'),
]

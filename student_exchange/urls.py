from django.urls import path
from .views import MarketplaceView, TravelListView

app_name = 'student_exchange'

urlpatterns = [
    path('marketplace/', MarketplaceView.as_view(), name='marketplace'),
    path('travel/', TravelListView.as_view(), name='travel_list'),
]

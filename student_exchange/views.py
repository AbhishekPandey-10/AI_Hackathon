from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MarketItem, TravelRequest

class MarketplaceView(LoginRequiredMixin, ListView):
    model = MarketItem
    template_name = 'student_exchange/marketplace.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        return MarketItem.objects.filter(status='available').order_by('-created_at')

class TravelListView(LoginRequiredMixin, ListView):
    model = TravelRequest
    template_name = 'student_exchange/travel_list.html'
    context_object_name = 'trips'
    
    def get_queryset(self):
        # Show active trips ordered by departure time
        return TravelRequest.objects.filter(is_active=True).order_by('departure_time')

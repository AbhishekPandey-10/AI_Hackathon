from django.contrib import admin
from .models import MarketItem, StudyResource, TravelRequest, LostItem

@admin.register(MarketItem)
class MarketItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'status', 'seller')
    list_filter = ('category', 'status')
    search_fields = ('title', 'description')

@admin.register(StudyResource)
class StudyResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject_code', 'resource_type', 'uploader')
    list_filter = ('resource_type', 'subject_code')

@admin.register(TravelRequest)
class TravelRequestAdmin(admin.ModelAdmin):
    list_display = ('destination', 'departure_time', 'mode', 'is_active')
    list_filter = ('destination', 'is_active')

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_type', 'location', 'is_resolved')
    list_filter = ('item_type', 'is_resolved')

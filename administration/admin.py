from django.contrib import admin
from .models import FeeStatus, Complaint

@admin.register(FeeStatus)
class FeeStatusAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'total_amount', 'due_amount', 'status')
    list_filter = ('semester',)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'category', 'status', 'created_at')
    list_filter = ('status', 'category')

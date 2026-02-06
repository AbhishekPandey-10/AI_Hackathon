from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'enrollment_number', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'enrollment_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'enrollment_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

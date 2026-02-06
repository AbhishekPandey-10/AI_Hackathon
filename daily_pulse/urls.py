from django.urls import path
from .views import rate_meal

app_name = 'daily_pulse'

urlpatterns = [
    path('rate/<int:menu_id>/', rate_meal, name='rate_meal'),
]

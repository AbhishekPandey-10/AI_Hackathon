from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import MessMenu, MealRating
from .forms import MealRatingForm

@login_required
@require_POST
def rate_meal(request, menu_id):
    menu_item = get_object_or_404(MessMenu, id=menu_id)
    form = MealRatingForm(request.POST)
    
    if form.is_valid():
        # specific logic: update if exists, or create new
        rating, created = MealRating.objects.update_or_create(
            user=request.user,
            menu_item=menu_item,
            defaults={'rating': form.cleaned_data['rating']}
        )
        messages.success(request, "Feedback recorded!")
    else:
        messages.error(request, "Error submitting feedback.")
        
    return redirect('dashboard')

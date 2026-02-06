from django import forms
from .models import MealRating

class MealRatingForm(forms.ModelForm):
    class Meta:
        model = MealRating
        fields = ['rating']
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'hidden peer'}),
        }

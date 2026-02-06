from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['category', 'title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

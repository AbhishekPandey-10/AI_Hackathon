from django.db import models
from django.utils import timezone

class MessMenu(models.Model):
    MEAL_TYPES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Snacks', 'Snacks'),
        ('Dinner', 'Dinner'),
    ]
    
    date = models.DateField(default=timezone.now)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    dish_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, help_text="Sides, deserts, etc.")
    calories = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        # Ensures you can't have two "Lunch" entries for the same day
        unique_together = ('date', 'meal_type')
        ordering = ['date', 'meal_type']

    def __str__(self):
        return f"{self.date} - {self.meal_type}: {self.dish_name}"

class Notice(models.Model):
    URGENCY_LEVELS = [
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
        ('critical', 'Critical'),
    ]
    
    title = models.CharField(max_length=200)
    summary = models.TextField(help_text="AI-generated summary of the email/notice")
    urgency = models.CharField(max_length=20, choices=URGENCY_LEVELS, default='normal')
    source = models.CharField(max_length=100, help_text="e.g., 'Dean Academics' or 'Estate Office'")
    created_at = models.DateTimeField(auto_now_add=True)
    attachment_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class MealRating(models.Model):
    RATING_CHOICES = [(1, 'Low'), (3, 'Medium'), (5, 'High')]
    
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MessMenu, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'menu_item')

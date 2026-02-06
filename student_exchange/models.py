from django.db import models
from django.conf import settings

class MarketItem(models.Model):
    # Custom categories from your notes
    CATEGORY_CHOICES = [
        ('book', 'Books'),
        ('cycle', 'Cycles'),
        ('electronics', 'Electronics'),
        ('garbage', 'Garbage to College (Scrap/Recycle)'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
    ]
    
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField(help_text="Condition, brand, or specific details")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='market_items/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title} - ₹{self.price}"

class StudyResource(models.Model):
    # "Study Material" branch from your notes
    RESOURCE_TYPES = [
        ('pyq', 'Previous Year Question (PYQ)'),
        ('notes', 'Topper Notes'),
        ('video', 'Video Lecture Link'),
    ]
    
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    subject_code = models.CharField(max_length=20, help_text="e.g., CS101, MA201")
    file = models.FileField(upload_to='study_materials/', blank=True, null=True, help_text="Upload PDF/Images")
    link = models.URLField(blank=True, null=True, help_text="YouTube/Drive link for videos")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject_code} - {self.title} ({self.get_resource_type_display()})"

class TravelRequest(models.Model):
    # "Travel Sharing" branch from your notes
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100, help_text="e.g., Chandigarh, Delhi Airport")
    departure_time = models.DateTimeField()
    mode = models.CharField(max_length=50, help_text="Cab, Auto, or Personal Vehicle")
    capacity = models.PositiveIntegerField(default=1, help_text="Seats available / People needed")
    contact_info = models.CharField(max_length=100, help_text="Phone number or WhatsApp link")
    is_active = models.BooleanField(default=True)
    
    # "Safety" feature placeholder
    is_verified_traveler = models.BooleanField(default=False, help_text="Verified by college ID")

    def __str__(self):
        return f"Trip to {self.destination} at {self.departure_time}"

class LostItem(models.Model):
    # "Site Police" branch from your notes
    TYPE_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    location = models.CharField(max_length=100, help_text="Where was it lost/found?")
    image = models.ImageField(upload_to='lost_found/', blank=True, null=True, help_text="Upload image for AI matching")
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.item_type.upper()}] {self.title}"

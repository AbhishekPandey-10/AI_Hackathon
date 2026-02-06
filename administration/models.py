from django.db import models
from django.conf import settings

class FeeStatus(models.Model):
    SEMESTER_CHOICES = [(i, f"Semester {i}") for i in range(1, 9)]
    
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    semester = models.PositiveIntegerField(choices=SEMESTER_CHOICES, default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total Semester Fee")
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_payment_date = models.DateField(null=True, blank=True)
    
    @property
    def due_amount(self):
        return self.total_amount - self.paid_amount

    @property
    def status(self):
        if self.due_amount <= 0:
            return "Paid"
        elif self.paid_amount > 0:
            return "Partial"
        return "Unpaid"

    def __str__(self):
        return f"{self.student.username} - Sem {self.semester} Fee"

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('hostel', 'Hostel/Room'),
        ('mess', 'Mess/Food'),
        ('security', 'Security'),
        ('academic', 'Academic'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    image = models.ImageField(upload_to='complaints/', blank=True, null=True, help_text="Evidence if any")
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"[{self.get_status_display()}] {self.title}"

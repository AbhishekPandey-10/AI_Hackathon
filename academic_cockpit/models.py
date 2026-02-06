from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Data Structures")
    code = models.CharField(max_length=20, unique=True, help_text="e.g. CS101")
    faculty_name = models.CharField(max_length=100, help_text="Professor Name")
    credits = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"{self.code} - {self.name}"

class TimetableSlot(models.Model):
    DAYS_OF_WEEK = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=50, help_text="e.g. LH-3, Block A")

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.day} {self.start_time} - {self.course.name}"

class Attendance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_lectures = models.PositiveIntegerField(default=0)
    attended_lectures = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    @property
    def percentage(self):
        if self.total_lectures == 0:
            return 0
        return round((self.attended_lectures / self.total_lectures) * 100, 1)

    def __str__(self):
        return f"{self.student.username} - {self.course.code}: {self.percentage}%"

class StudentResult(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, help_text="e.g. A, B+, F")
    semester = models.PositiveIntegerField(default=1)
    
    # Simple CGPA tracking (can be calculated, but storing for speed as per your note)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.code}: {self.grade}"

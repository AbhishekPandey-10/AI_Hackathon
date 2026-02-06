from django.contrib import admin
from .models import Course, TimetableSlot, Attendance, StudentResult

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'faculty_name', 'credits')
    search_fields = ('name', 'code')

@admin.register(TimetableSlot)
class TimetableSlotAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'course', 'location')
    list_filter = ('day',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'percentage')
    list_filter = ('course',)

@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade', 'semester')
    list_filter = ('semester', 'grade')

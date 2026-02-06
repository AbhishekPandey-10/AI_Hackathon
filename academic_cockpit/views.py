from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from .models import TimetableSlot, Attendance, StudentResult, Course

class AcademicDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'academic_cockpit/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # 1. Weekly Timetable Structure
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
        full_timetable = {}
        
        for day in days:
            # Fetch slots for this day, ordered by time
            slots = TimetableSlot.objects.filter(day=day).select_related('course').order_by('start_time')
            full_timetable[day] = slots

        context['timetable'] = full_timetable
        context['days'] = days # Pass list for iterating in template

        # 2. Detailed Attendance (Subject-wise)
        # We fetch all attendance records for this student
        context['attendance_records'] = Attendance.objects.filter(
            student=user
        ).select_related('course').order_by('course__name')

        # 3. Results / CGPA
        context['results'] = StudentResult.objects.filter(
            student=user
        ).select_related('course').order_by('-semester', 'course__code')
        
        # Calculate latest CGPA (simple average of stored CGPAs for now, or take the latest sem)
        latest_result = context['results'].first()
        context['current_cgpa'] = latest_result.cgpa if latest_result else "N/A"

        return context

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db.models import Sum, Count, Q
from daily_pulse.models import MessMenu, Notice, MealRating
from student_exchange.models import MarketItem, TravelRequest
from academic_cockpit.models import TimetableSlot, Attendance
from administration.models import FeeStatus
from .forms import SignUpForm

class SignUpView(TemplateView):
    template_name = 'users/signup.html'
    # ... existing code ...

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return self.render_to_response({'form': form})

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Determine "Current Meal" Logic
        current_hour = timezone.now().hour
        if current_hour < 10:
            meal_target = 'Breakfast'
        elif current_hour < 15:
            meal_target = 'Lunch'
        elif current_hour < 18:
            meal_target = 'Snacks'
        else:
            meal_target = 'Dinner'

        today = timezone.now().date()
        
        # Fetch the specific menu item for today + current time
        context['current_meal'] = MessMenu.objects.filter(
            date=today, 
            meal_type=meal_target
        ).first()
        
        context['meal_target_name'] = meal_target

        # 2. Fetch Notices (Top 3 most recent)
        context['notices'] = Notice.objects.all().order_by('-created_at')[:3]

        # 3. Exchange Stats
        
        # Count available "Garbage to College" or regular items
        market_count = MarketItem.objects.filter(status='available').count()
        
        # Count active trips for "Travel Sharing"
        trip_count = TravelRequest.objects.filter(is_active=True).count()
        
        # Get the latest item for the widget text
        latest_market_item = MarketItem.objects.filter(status='available').order_by('-created_at').first()

        context['market_count'] = market_count
        context['trip_count'] = trip_count
        context['latest_market_item'] = latest_market_item

        # 4. Academic Stats (Next Class)
        current_day_code = timezone.now().strftime('%a').upper() # e.g., 'FRI'
        current_time = timezone.now().time()
        
        # Find the next class for today that starts after right now
        next_class = TimetableSlot.objects.filter(
            day=current_day_code,
            start_time__gte=current_time
        ).order_by('start_time').first()

        context['next_class'] = next_class

        # 5. Calculate Overall Attendance
        # We sum all attended lectures and divide by total lectures across all courses
        attendance_agg = Attendance.objects.filter(student=self.request.user).aggregate(
            total_held=Sum('total_lectures'),
            total_attended=Sum('attended_lectures')
        )
        
        overall_attendance = 0
        if attendance_agg['total_held'] and attendance_agg['total_held'] > 0:
            overall_attendance = round(
                (attendance_agg['total_attended'] / attendance_agg['total_held']) * 100, 
                1
            )
            
        context['overall_attendance'] = overall_attendance
        context['attendance_color'] = '#ef4444' if overall_attendance < 75 else '#10b981'
        # Pre-calculate the gradient style to avoid IDE syntax errors in the template
        context['attendance_gradient_val'] = f"conic-gradient({context['attendance_color']} {overall_attendance}%, rgba(255,255,255,0.1) 0)"
        
        # 6. Administrative Stats (Fee)
        # Get the latest fee record for the student
        fee_record = FeeStatus.objects.filter(student=self.request.user).order_by('-semester').first()
        context['fee_record'] = fee_record

        # 7. Daily Pulse Stats (Feedback Graph)
        # Get ratings for today's meals
        today_ratings = MealRating.objects.filter(menu_item__date=today)
        total_ratings = today_ratings.count()
        
        feedback_stats = {
            'high': 0,
            'medium': 0,
            'low': 0
        }
        
        if total_ratings > 0:
            stats = today_ratings.aggregate(
                high=Count('id', filter=Q(rating=5)),
                medium=Count('id', filter=Q(rating=3)),
                low=Count('id', filter=Q(rating=1))
            )
            # Calculate percentages for the graph
            feedback_stats['high'] = int((stats['high'] / total_ratings) * 100)
            feedback_stats['medium'] = int((stats['medium'] / total_ratings) * 100)
            feedback_stats['low'] = int((stats['low'] / total_ratings) * 100)
            
        context['feedback_stats'] = feedback_stats

        return context

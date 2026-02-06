from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Complaint
from .forms import ComplaintForm

class ComplaintListView(LoginRequiredMixin, ListView):
    model = Complaint
    template_name = 'administration/complaints.html'
    context_object_name = 'complaints'
    
    def get_queryset(self):
        return Complaint.objects.filter(student=self.request.user).order_by('-created_at')

class ComplaintCreateView(LoginRequiredMixin, CreateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'administration/complaint_form.html'
    success_url = reverse_lazy('administration:complaint_list')
    
    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Lead
from django.urls import reverse_lazy

# ListView for leads
class LeadListView(ListView):
    model = Lead
    template_name = 'lead_management_system/lead_list.html'
    context_object_name = 'leads'

# CreateView for new lead
class LeadCreateView(CreateView):
    model = Lead
    template_name = 'lead_management_system/lead_form.html'
    fields = ['name', 'email', 'phone_number', 'status', 'source']
    success_url = reverse_lazy('lead_list')

# UpdateView for updating lead details
class LeadUpdateView(UpdateView):
    model = Lead
    template_name = 'lead_management_system/lead_form.html'
    fields = ['name', 'email', 'phone_number', 'status', 'source']
    success_url = reverse_lazy('lead_list')

# DeleteView for deleting a lead
class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'lead_management_system/lead_confirm_delete.html'
    success_url = reverse_lazy('lead_list')

# View to summarize leads by status
def lead_summary(request):
    total_leads = Lead.objects.all().count()
    new_leads = Lead.objects.filter(status='New').count()
    in_progress_leads = Lead.objects.filter(status='In Progress').count()
    converted_leads = Lead.objects.filter(status='Converted').count()
    rejected_leads = Lead.objects.filter(status='Rejected').count()

    context = {
        'total_leads': total_leads,
        'new_leads': new_leads,
        'in_progress_leads': in_progress_leads,
        'converted_leads': converted_leads,
        'rejected_leads': rejected_leads,
    }

    return render(request, 'lead_management_system/lead_summary.html', context)

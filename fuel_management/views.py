# fuel_management/views.py
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FuelLog
from .forms import FuelLogForm
from django.template.loader import render_to_string
from weasyprint import HTML

class HomeView(TemplateView):
    template_name = 'fuel_management/home.html'

def fuel_log_list(request):
    fuel_logs = FuelLog.objects.all()
    return render(request, 'fuel_management/fuel_log_list.html', {'fuel_logs': fuel_logs})

def add_fuel_log(request):
    if request.method == 'POST':
        form = FuelLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fuel_log_list')
    else:
        form = FuelLogForm()
    return render(request, 'fuel_management/add_fuel_log.html', {'form': form})

def generate_pdf(request):
    fuel_logs = FuelLog.objects.all()
    html_string = render_to_string('fuel_management/pdf_template.html', {'fuel_logs': fuel_logs})
    pdf_file = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="fuel_logs.pdf"'
    return response

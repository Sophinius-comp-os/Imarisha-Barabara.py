# imarisha_barabara/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fuel-management/', include('fuel_management.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Add this line
]

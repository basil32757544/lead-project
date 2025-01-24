"""
URL configuration for lead_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import LeadListView, LeadCreateView, LeadUpdateView, LeadDeleteView, lead_summary

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', LeadListView.as_view(), name='lead_list'),  # List all leads
    path('create/', LeadCreateView.as_view(), name='lead_create'),  # Create a new lead
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),  # Update a lead
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),  # Delete a lead
    path('summary/', lead_summary, name='lead_summary'),  # View summary
]

from django.shortcuts import render
from django.views import generic
from .models import (
    UserProfile,
    Certificate,
    Education,
    WorkExperience
)

from portfolio.models import Portfolio

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        certificate_items = Certificate.objects.filter(is_active=True)
        portfolio_items = Portfolio.objects.filter(is_active=True)
        education_items = Education.objects.all()
        workExperience_items = WorkExperience.objects.all()

        context["certificate_items"] = certificate_items
        context["portfolio_items"] = portfolio_items
        context["education_items"] = education_items

        return context








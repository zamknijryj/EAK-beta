from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'homepage/homepage.html'


class RejstrZolnierzy(TemplateView):
    template_name = 'homepage/rejestr.html'


class AbcEak(TemplateView):
    template_name = 'homepage/abc.html'

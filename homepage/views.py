from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'homepage/homepage.html'


class RejstrZolnierzy(TemplateView):
    template_name = 'homepage/rejestr.html'


class AbcEak(TemplateView):
    template_name = 'homepage/abc.html'


class Majordom(TemplateView):
    template_name = 'homepage/majordom_koronny.html'


class ObronaTerytorialna(TemplateView):
    template_name = 'homepage/obrona_terytorialna.html'

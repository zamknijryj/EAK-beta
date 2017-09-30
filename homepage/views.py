from django.shortcuts import render
from django.views.generic import TemplateView


####### MENU #######


class Homepage(TemplateView):
    template_name = 'homepage/homepage.html'


class RejstrZolnierzy(TemplateView):
    template_name = 'homepage/rejestr.html'


class AbcEak(TemplateView):
    template_name = 'homepage/abc.html'


class Rekrutacja(TemplateView):
    template_name = 'homepage/rekrutacja.html'


####### KARTY #######


class Majordom(TemplateView):
    template_name = 'homepage/majordom_koronny.html'


class ObronaTerytorialna(TemplateView):
    template_name = 'homepage/obrona_terytorialna.html'


class SilyOperacyjne(TemplateView):
    template_name = 'homepage/sily_operacyjne.html'


class ZakonRycerzy(TemplateView):
    template_name = 'homepage/zakon.html'


class Gwardia(TemplateView):
    template_name = 'homepage/gwardia.html'


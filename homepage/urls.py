from django.contrib.auth.urls import url
from .views import (
    Homepage,
    RejstrZolnierzy,
    AbcEak,
    Majordom,
    ObronaTerytorialna
)

urlpatterns = [
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^rejestr-zolnierzy/$', RejstrZolnierzy.as_view(), name='rejestr-zolnierzy'),
    url(r'^abc/$', AbcEak.as_view(), name='abc-eak'),
    url(r'^majordom-koronny/$', Majordom.as_view(), name='majordom'),
    url(r'^krolewska-obrona-terytorialna/$', ObronaTerytorialna.as_view(), name='OT')
]

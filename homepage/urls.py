from django.contrib.auth.urls import url
from .views import (
    Homepage,
    RejstrZolnierzy,
    AbcEak,
    Rekrutacja,
    Majordom,
    ObronaTerytorialna,
    SilyOperacyjne,
    ZakonRycerzy,
    Gwardia
)

urlpatterns = [
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^rejestr-zolnierzy/$', RejstrZolnierzy.as_view(), name='rejestr-zolnierzy'),
    url(r'^rekrutacja/$', Rekrutacja.as_view(), name='rekrutacja'),
    url(r'^abc/$', AbcEak.as_view(), name='abc-eak'),
    url(r'^majordom-koronny/$', Majordom.as_view(), name='majordom'),
    url(r'^krolewska-obrona-terytorialna/$', ObronaTerytorialna.as_view(), name='OT'),
    url(r'^krolewskie-sily-operacyjne/$', SilyOperacyjne.as_view(), name='sily-operacyjne'),
    url(r'^zakon-rycerzy-krola-edwarda/$', ZakonRycerzy.as_view(), name='zakon'),
    url(r'^gwardia-krolewska/$', Gwardia.as_view(), name='gwardia')
]

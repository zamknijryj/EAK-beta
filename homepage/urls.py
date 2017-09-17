from django.contrib.auth.urls import url
from .views import (
    Homepage,
    RejstrZolnierzy,
    AbcEak
)

urlpatterns = [
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^rejestr-zolnierzy/$', RejstrZolnierzy.as_view(), name='rejestr-zolnierzy'),
    url(r'^abc/$', AbcEak.as_view(), name='abc-eak')

]

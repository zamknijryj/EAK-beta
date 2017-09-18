from django.contrib.auth.urls import url
from .views import (
    Aktualnosci,
    AktualnosciDetail,
    test
)

urlpatterns = [
    url(r'^$', Aktualnosci.as_view(), name='aktualnosci'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        test,
        name='test'),
]

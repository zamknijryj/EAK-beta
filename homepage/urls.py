from django.contrib.auth.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^rejestr-zolnierzy', views.rejestr_zolnierzy, name='rejestr-zolnierzy'),

]

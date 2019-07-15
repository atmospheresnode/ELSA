from django.conf.urls import url
from . import views



app_name='context'
urlpatterns = [
    url(r'^$', views.context, name='context'),
    url(r'^investigations/$', views.investigations, name='investigations'),
    url(r'^instruments/$', views.instruments, name='instruments'),
    url(r'^instrument_hosts/$', views.instrument_hosts, name='instrument_hosts'),

]

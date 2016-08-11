from django.conf.urls import url
from formadores.views import InicioView, VinculosView, LegalizacionView, LegalizacionCompletaView, TransportesView
from formadores.views import NuevaSolicitudTransportesView, SubirSoporteTransportesView

urlpatterns = [
    url(r'^$', InicioView.as_view()),
    url(r'^(?P<cedula>[0-9]+)/$', VinculosView.as_view()),
    url(r'^(?P<cedula>[0-9]+)/legalizacion/$', LegalizacionView.as_view()),
    url(r'^(?P<cedula>[0-9]+)/legalizacion/completo/$', LegalizacionCompletaView.as_view()),
    url(r'^(?P<cedula>[0-9]+)/transportes/$', TransportesView.as_view()),
    url(r'^(?P<cedula>[0-9]+)/transportes/nueva/$', NuevaSolicitudTransportesView.as_view()),
    url(r'^(?P<cedula>[0-9]+)/transportes/soporte/(?P<id_soporte>[0-9]+)/$', SubirSoporteTransportesView.as_view()),
]
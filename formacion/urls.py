from django.conf.urls import url
from formacion.views import ListaPreinscritosView, NuevoPreinscritoView, UpdatePreinscritoView,DeletePreinscritoView
from formacion.views import ListaRevisionView
from formacion.views import ListaTransportesView, ListaTransportesAprobadasFinancieraView, ListaTransportesRechazadasView, ListaTransportesPendientesView
from formacion.views import TransporteFormView, TransporteFormUpdateView
from formacion.views import ListaTransportesConsignadasView, ListaTransportesAprobadasLideresView

urlpatterns = [
    url(r'^preinscritos/$', ListaPreinscritosView.as_view()),
    url(r'^preinscritos/nuevo/$', NuevoPreinscritoView.as_view()),
    url(r'^preinscritos/editar/(?P<pk>[0-9]+)/$', UpdatePreinscritoView.as_view()),
    url(r'^preinscritos/eliminar/(?P<pk>[0-9]+)/$', DeletePreinscritoView.as_view()),

    url(r'^revision/$', ListaRevisionView.as_view()),

    url(r'^transportes/$', ListaTransportesView.as_view()),


    url(r'^transportes/consignadas/(?P<id>[0-9]+)/$', ListaTransportesConsignadasView.as_view()),
    url(r'^transportes/aprobadasfinanciera/(?P<id>[0-9]+)/$', ListaTransportesAprobadasFinancieraView.as_view()),
    url(r'^transportes/aprobadaslideres/(?P<id>[0-9]+)/$', ListaTransportesAprobadasLideresView.as_view()),
    url(r'^transportes/rechazadas/(?P<id>[0-9]+)/$', ListaTransportesRechazadasView.as_view()),


    url(r'^transportes/pendientes/(?P<id>[0-9]+)/$', ListaTransportesPendientesView.as_view()),
    url(r'^transportes/pendientes/(?P<id>[0-9]+)/estado/(?P<id_solicitud>[0-9]+)/$', TransporteFormView.as_view()),
    url(r'^transportes/pendientes/(?P<id>[0-9]+)/editar/(?P<id_solicitud>[0-9]+)/$', TransporteFormUpdateView.as_view()),
]
from django.conf.urls import url
from financiera.views import TransportesView, TransportesEstadoView, TransportesEliminarView
from financiera.views import TransportesCreateView, TransportesUpdateView
from financiera.views import TransportesAprobadasFinancieraView, TransportesAprobadasLideresView, TransportesRechazadasView, TransportesPendientesView
from financiera.views import TransportesConsignadasFinancieraView
from financiera.views import SemanasListView, FormadoresCronogramaListView, CronogramaFormadorView
from financiera.views import CronogramaFormadorNuevoView, CronogramaFormadorUpdateView, CronogramaFormadorDeleteView
from financiera.views import ContratosListView

urlpatterns = [
    url(r'^transportes/$', TransportesView.as_view()),

    url(r'^transportes/consignadas/(?P<id_formador>\w+)/$', TransportesConsignadasFinancieraView.as_view()),
    url(r'^transportes/consignadas/(?P<id_formador>\w+)/estado/(?P<pk>\w+)/$', TransportesEstadoView.as_view()),
    url(r'^transportes/consignadas/(?P<id_formador>\w+)/editar/(?P<pk>\w+)/$', TransportesUpdateView.as_view()),
    url(r'^transportes/consignadas/(?P<id_formador>\w+)/eliminar/(?P<pk>\w+)/$', TransportesEliminarView.as_view()),


    url(r'^transportes/aprobadasfinanciera/(?P<id_formador>\w+)/$', TransportesAprobadasFinancieraView.as_view()),
    url(r'^transportes/aprobadasfinanciera/(?P<id_formador>\w+)/estado/(?P<pk>\w+)/$', TransportesEstadoView.as_view()),
    url(r'^transportes/aprobadasfinanciera/(?P<id_formador>\w+)/editar/(?P<pk>\w+)/$', TransportesUpdateView.as_view()),
    url(r'^transportes/aprobadasfinanciera/(?P<id_formador>\w+)/eliminar/(?P<pk>\w+)/$', TransportesEliminarView.as_view()),


    url(r'^transportes/aprobadaslideres/(?P<id_formador>\w+)/$', TransportesAprobadasLideresView.as_view()),
    url(r'^transportes/aprobadaslideres/(?P<id_formador>\w+)/estado/(?P<pk>\w+)/$', TransportesEstadoView.as_view()),
    url(r'^transportes/aprobadaslideres/(?P<id_formador>\w+)/editar/(?P<pk>\w+)/$', TransportesUpdateView.as_view()),
    url(r'^transportes/aprobadaslideres/(?P<id_formador>\w+)/eliminar/(?P<pk>\w+)/$', TransportesEliminarView.as_view()),


    url(r'^transportes/rechazadas/(?P<id_formador>\w+)/$', TransportesRechazadasView.as_view()),
    url(r'^transportes/rechazadas/(?P<id_formador>\w+)/estado/(?P<pk>\w+)/$', TransportesEstadoView.as_view()),
    url(r'^transportes/rechazadas/(?P<id_formador>\w+)/editar/(?P<pk>\w+)/$', TransportesUpdateView.as_view()),
    url(r'^transportes/rechazadas/(?P<id_formador>\w+)/eliminar/(?P<pk>\w+)/$', TransportesEliminarView.as_view()),


    url(r'^transportes/pendientes/(?P<id_formador>\w+)/$', TransportesPendientesView.as_view()),
    url(r'^transportes/pendientes/(?P<id_formador>\w+)/estado/(?P<pk>\w+)/$', TransportesEstadoView.as_view()),
    url(r'^transportes/pendientes/(?P<id_formador>\w+)/editar/(?P<pk>\w+)/$', TransportesUpdateView.as_view()),
    url(r'^transportes/pendientes/(?P<id_formador>\w+)/eliminar/(?P<pk>\w+)/$', TransportesEliminarView.as_view()),



    url(r'^transportes/estado/(?P<pk>\w+)/$', TransportesEstadoView.as_view()),
    url(r'^transportes/nuevo/$', TransportesCreateView.as_view()),
    url(r'^transportes/eliminar/(?P<pk>\w+)/$', TransportesEliminarView.as_view()),
    url(r'^transportes/editar/(?P<pk>\w+)/$', TransportesUpdateView.as_view()),


    url(r'^cronograma/$', SemanasListView.as_view()),
    url(r'^cronograma/semana/(?P<semana_id>\w+)/$', FormadoresCronogramaListView.as_view()),
    url(r'^cronograma/semana/(?P<semana_id>[0-9]+)/editar/(?P<id>[0-9]+)/$', CronogramaFormadorView.as_view()),
    url(r'^cronograma/semana/(?P<semana_id>[0-9]+)/editar/(?P<id>[0-9]+)/nuevo/$', CronogramaFormadorNuevoView.as_view()),
    url(r'^cronograma/semana/(?P<semana_id>[0-9]+)/editar/(?P<id>[0-9]+)/entrada/(?P<id_entrada>[0-9]+)/$', CronogramaFormadorUpdateView.as_view()),
    url(r'^cronograma/semana/(?P<semana_id>[0-9]+)/editar/(?P<id>[0-9]+)/eliminar/(?P<id_entrada>[0-9]+)/$', CronogramaFormadorDeleteView.as_view()),


    url(r'^contratos/$', ContratosListView.as_view()),
]
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', lista_nomencladores,name='lista_nomencladores'),
    path('comentarista/crear', ComentaristaCreate.as_view(),name='crea_comentarista'),
    path('comentarista/lista', ComentaristaList.as_view(),name='lista_comentarista'),
    path('linea_financiamiento/crear', LineaFinaciamientoCreate.as_view(),name='crea_linea_financiamiento'),
    path('linea_financiamiento/lista', LineaFinaciamientoList.as_view(),name='lista_linea_financiamiento'),
    path('instrumento_pago/crear', InstrumentoPagoCreate.as_view(),name='crea_instrumento_pago'),
    path('instrumento_pago/lista', InstrumentoPagoList.as_view(),name='lista_instrumento_pago'),
    path('condicion_entrega/crear', CondicionEntregaCreate.as_view(),name='crea_condicion_entrega'),
    path('condicion_entrega/lista', CondicionEntregaList.as_view(),name='lista_condicion_entrega'),
    path('documento_pago/crear', DocumentoPagoCreate.as_view(),name='crea_documento_pago'),
    path('documento_pago/lista', DocumentoPagoList.as_view(),name='lista_documento_pago'),
    path('documento_prestamista/crear', DocumentoPrestamistaCreate.as_view(),name='crea_documento_prestamista'),
    path('documento_prestamista/lista', DocumentoPrestamistaList.as_view(),name='lista_documento_prestamista'),
    path('aerolinea/crear', AerolineaCreate.as_view(),name='crea_aerolinea'),
    path('aerolinea/lista', AerolineaList.as_view(),name='lista_aerolinea'),
    path('aeropuerto_embarque/crear', AeropuertoEmbarqueCreate.as_view(),name='crea_aeropuerto_embarque'),
    path('aeropuerto_embarque/lista', AeropuertoEmbarqueList.as_view(),name='lista_aeropuerto_embarque'),
    path('agente_carga/crear', AgenteCargaCreate.as_view(),name='crea_agente_carga'),
    path('agente_carga/lista', AgenteCargaList.as_view(),name='lista_agente_carga'),
    path('almacen_destino/crear', AlmacenDestinoCreate.as_view(),name='crea_almacen_destino'),
    path('almacen_destino/lista', AlmacenDestinoList.as_view(),name='lista_almacen_destino'),
    path('naviera/crear', NavieraCreate.as_view(),name='crea_naviera'),
    path('naviera/lista', NavieraList.as_view(),name='lista_naviera'),
    path('puerto_embarque/crear', PuertoEmbarqueCreate.as_view(),name='crea_puerto_embarque'),
    path('puerto_embarque/lista', PuertoEmbarqueList.as_view(),name='lista_puerto_embarque'),
    path('transitaria/crear', TransitariaCreate.as_view(),name='crea_transitaria'),
    path('transitaria/lista', TransitariaList.as_view(),name='lista_transitaria'),


]
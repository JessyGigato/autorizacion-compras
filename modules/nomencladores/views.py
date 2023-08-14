from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import CreateView, ListView
from .models import *
from .forms import  * 
from django.urls import reverse_lazy

def lista_nomencladores(request):
    return TemplateResponse(request,"nomencladores/lista_nomencladores.html")

class ComentaristaCreate(CreateView):
    model = Comentarista
    form_class = ComentaristaForm
    template_name = "nomencladores/comentarista/crear_comentarista.html"
    success_url = reverse_lazy('nomencladores:lista_comentarista')

class ComentaristaList(ListView):
    model = Comentarista
    template_name = "nomencladores/comentarista/lista_comentaristas.html"

class LineaFinaciamientoCreate(CreateView):
    model = LineaFinanciamiento
    form_class = LineaFinanciamientoForm
    template_name = "nomencladores/linea_financiamiento/crear_linea_financiamiento.html"
    success_url = reverse_lazy('nomencladores:lista_linea_financiamiento')

class LineaFinaciamientoList(ListView):
    model = LineaFinanciamiento
    template_name = "nomencladores/linea_financiamiento/lista_linea_financiamiento.html"

class InstrumentoPagoCreate(CreateView):
    model = InstrumentoPago
    form_class = InstrumentoPagoForm
    template_name = "nomencladores/instrumento_pago/crear_instrumento_pago.html"
    success_url = reverse_lazy('nomencladores:lista_instrumento_pago')

class InstrumentoPagoList(ListView):
    model = InstrumentoPago
    template_name = "nomencladores/instrumento_pago/lista_instrumento_pago.html"

class CondicionEntregaCreate(CreateView):
    model = CondicionEntrega
    form_class = CondicionEntregaForm
    template_name = "nomencladores/condicion_entrega/crear_condicion_entrega.html"
    success_url = reverse_lazy('nomencladores:lista_condicion_entrega')

class CondicionEntregaList(ListView):
    model = CondicionEntrega
    template_name = "nomencladores/condicion_entrega/lista_condicion_entrega.html"

class DocumentoPagoCreate(CreateView):
    model = DocumentoPago
    form_class = DocumentoPagoForm
    template_name = "nomencladores/documento_pago/crear_documento_pago.html"
    success_url = reverse_lazy('nomencladores:lista_documento_pago')

class DocumentoPagoList(ListView):
    model = DocumentoPago
    template_name = "nomencladores/documento_pago/lista_documento_pago.html"   

class DocumentoPrestamistaCreate(CreateView):
    model = DocumentoPrestamista
    form_class = DocumentoPrestamistaForm
    template_name = "nomencladores/documento_prestamista/crear_documento_prestamista.html"
    success_url = reverse_lazy('nomencladores:lista_documento_prestamista')

class DocumentoPrestamistaList(ListView):
    model = DocumentoPrestamista
    template_name = "nomencladores/documento_prestamista/lista_documento_prestamista.html"

class AerolineaCreate(CreateView):
    model = Aerolinea
    form_class = AerolineaForm
    template_name = "nomencladores/aerolinea/crear_aerolinea.html"
    success_url = reverse_lazy('nomencladores:lista_aerolinea')

class AerolineaList(ListView):
    model = Aerolinea
    template_name = "nomencladores/aerolinea/lista_aerolinea.html"

class AeropuertoEmbarqueCreate(CreateView):
    model = AeropuertoEmbarque
    form_class = AeropuertoEmbarqueForm
    template_name = "nomencladores/aeropuerto_embarque/crear_aeropuerto_embarque.html"
    success_url = reverse_lazy('nomencladores:lista_aeropuerto_embarque')

class AeropuertoEmbarqueList(ListView):
    model = AeropuertoEmbarque
    template_name = "nomencladores/aeropuerto_embarque/lista_aeropuerto_embarque.html"

class AgenteCargaCreate(CreateView):
    model = AgenteCarga
    form_class = AgenteCargaForm
    template_name = "nomencladores/agente_carga/crear_agente_carga.html"
    success_url = reverse_lazy('nomencladores:lista_agente_carga')

class AgenteCargaList(ListView):
    model = AgenteCarga
    template_name = "nomencladores/agente_carga/lista_agente_carga.html"

class AlmacenDestinoCreate(CreateView):
    model = AlmacenDestino
    form_class = AlmacenDestinoForm
    template_name = "nomencladores/almacen_destino/crear_almacen_destino.html"
    success_url = reverse_lazy('nomencladores:lista_almacen_destino')

class AlmacenDestinoList(ListView):
    model = AlmacenDestino
    template_name = "nomencladores/almacen_destino/lista_almacen_destino.html"

class NavieraCreate(CreateView):
    model = Naviera
    form_class = NavieraForm
    template_name = "nomencladores/naviera/crear_naviera.html"
    success_url = reverse_lazy('nomencladores:lista_naviera')

class NavieraList(ListView):
    model = Naviera
    template_name = "nomencladores/naviera/lista_naviera.html"

class PuertoEmbarqueCreate(CreateView):
    model = PuertoEmbarque
    form_class = PuertoEmbarqueForm
    template_name = "nomencladores/puerto_embarque/crear_puerto_embarque.html"
    success_url = reverse_lazy('nomencladores:lista_puerto_embarque')

class PuertoEmbarqueList(ListView):
    model = PuertoEmbarque
    template_name = "nomencladores/puerto_embarque/lista_puerto_embarque.html"

class TransitariaCreate(CreateView):
    model = Transitaria
    form_class = TransitariaForm
    template_name = "nomencladores/transitaria/crear_transitaria.html"
    success_url = reverse_lazy('nomencladores:lista_transitaria')

class TransitariaList(ListView):
    model = Transitaria
    template_name = "nomencladores/transitaria/lista_transitaria.html"

#maaaaaaaaal
def grupo_productos_view(request):
    if request.method == 'POST':
        if 'agregar' in request.POST:
            valor = request.POST['nombre']
            
        form = GrupoProductosForm(request.POST)
        if form.is_valid():
            return form
    else:
        form = GrupoProductosForm()
    return render(request, 'grupo/grupo.html', {'form': form})





'''
class BuscarForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    
def mi_vista(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mi_lista = ...  # Obtener la lista a buscar
            return render(request, 'mi_template.html', {'nombre': nombre, 'mi_lista': mi_lista})
    else:
        form = BuscarForm()
    return render(request, 'mi_template.html', {'form': form})
'''
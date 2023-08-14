from django import forms
from .models import *
from modules.usuario.models import Usuario

class ComentaristaForm(forms.ModelForm):
    nombre = forms.ModelChoiceField(queryset=Usuario.objects.all())

    class Meta:
        model = Comentarista
        fields = [
            'certificado',
            'nombre',
        ] 
        labels = {
            'certificado': 'Certificado',
            'nombre': 'Nombre',
        }

class LineaFinanciamientoForm(forms.ModelForm):
    moneda = forms.ModelChoiceField(queryset=Moneda.objects.all())
    instrumento_pago = forms.ModelChoiceField(queryset=InstrumentoPago.objects.all())

    class Meta:
        model = LineaFinanciamiento
        fields = [
            'codigo',
            'descripcion',
            'activa',
            'moneda',
            'expira',
            'instrumento_pago',
            'monto_financiamiento',
            'dias_revolvencia',
            'monto_total',
            'dias',
            'interes',
            'revisa',
        ] 
        labels = {
            'codigo': 'Código',
            'descripcion':'Descripción',
            'activa':'Activa',
            'moneda': 'Moneda',
            'expira': 'Expira',
            'instrumento_pago': 'Instrumento de pago',
            'monto_financiamiento': 'Monto Financiamiento',
            'dias_revolvencia': 'Días de resolvencia',
            'monto_total': 'Monto total',
            'dias': 'Días',
            'interes': 'Interés',
            'revisa': 'Revisa',
        }

class InstrumentoPagoForm(forms.ModelForm):

    class Meta:
        model = InstrumentoPago
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class CondicionEntregaForm(forms.ModelForm):
    
    class Meta:
        model = CondicionEntrega
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class DocumentoPagoForm(forms.ModelForm):
    
    class Meta:
        model = DocumentoPago
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class DocumentoPrestamistaForm(forms.ModelForm):
    
    class Meta:
        model = DocumentoPrestamista
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class AerolineaForm(forms.ModelForm):
    
    class Meta:
        model = Aerolinea
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class AeropuertoEmbarqueForm(forms.ModelForm):
    
    class Meta:
        model = AeropuertoEmbarque
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class AgenteCargaForm(forms.ModelForm):
    
    class Meta:
        model = AgenteCarga
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class AlmacenDestinoForm(forms.ModelForm):
    
    class Meta:
        model = AlmacenDestino
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class NavieraForm(forms.ModelForm):
    
    class Meta:
        model = Naviera
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class PuertoEmbarqueForm(forms.ModelForm):
    
    class Meta:
        model = PuertoEmbarque
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class TransitariaForm(forms.ModelForm):
    
    class Meta:
        model = Transitaria
        fields = [
            'codigo',
            'nombre',
        ] 
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
        }

class GrupoProductosForm(forms.ModelForm):

    class Meta:
        model = GrupoProductos
        fields = [
            'division_familia',
            'descripcion',
            'comentarista',
            'division_pertenecia',
            'productos',

        ] 
        labels = {
            'division_familia': 'Division-Familia',
            'descripcion': 'Descripción',
            'comentarista':'Comentarista',
            'division_pertenecia':'Division-Pertenecia',
            'productos': 'Productos',
        }

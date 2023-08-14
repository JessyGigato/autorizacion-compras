from django.contrib import admin
from .models import Moneda, Comentarista,LineaFinanciamiento

# Register your models here.
admin.site.register(Moneda)
admin.site.register(Comentarista)
admin.site.register(LineaFinanciamiento)

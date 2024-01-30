from django.contrib import admin

from .models import Motorista
from .models import Carro


admin.site.register(Motorista)
admin.site.register(Carro)

from django.contrib import admin
from gestionpedidos.models import Clientes, Articulos, Pedidos

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono")
    search_fields = ("nombre", "telefono")

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    list_filter = ("nombre",)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)

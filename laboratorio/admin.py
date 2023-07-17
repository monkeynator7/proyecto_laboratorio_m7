from django.contrib import admin
from .models import Laboratorio, Producto, DirectorGeneral

# Register your models here.
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ['nombre']
    ordering = ('nombre',)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    list_display_links = ['nombre', 'laboratorio']
    ordering = ('nombre', 'laboratorio')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_display_links = ['nombre', 'laboratorio']
    ordering = ('nombre', 'laboratorio')
    list_filter = ('nombre', 'laboratorio')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(DirectorGeneral, DirectorAdmin)
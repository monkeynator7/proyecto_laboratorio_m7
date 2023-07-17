from django.db import models
import datetime

# Create your models here.
year_choice = []
for r in range(2015, (datetime.datetime.now().year+1)):
    year_choice.append((r,r))

def year_actual():
    return datetime.date.today().year

class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre')
    ciudad = models.CharField(verbose_name='Ciudad', default='sin especificar')
    pais = models.CharField(verbose_name='Pais', default='sin especificar')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre Director')
    laboratorio = models.OneToOneField('Laboratorio', on_delete=models.CASCADE)
    especialidad = models.CharField(verbose_name='Especialidad', default='sin especificar')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        db_table = 'Director General'
        verbose_name = 'Director General'
        verbose_name_plural ='Directores Generales'

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(verbose_name='Nombre Producto')
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.IntegerField(choices=year_choice, default=year_actual, verbose_name='Fecha de Fabricación')
    p_costo = models.DecimalField(null=False, decimal_places=2, max_digits=10, verbose_name='Costo Fabricación')
    p_venta = models.DecimalField(null=False, decimal_places=2, max_digits=10, verbose_name='Precio Venta')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')


    def __str__(self):
        return self.nombre

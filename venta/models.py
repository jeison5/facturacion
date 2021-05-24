from django.db import models
from django.contrib import auth
from django.db.models.aggregates import Max
from django.db.models.expressions import F
from django.db.models.fields import CharField, DecimalField
from django.db.models.query import FlatValuesListIterable
from django.utils.timezone import now

# Create your models here.

class Categoria(models.Model):
    nombre_categoria =  models.CharField(max_length = 50, null=False, blank=False, verbose_name="Nombre")
    descripcion_categoria = models.CharField(max_length=255, null=False, blank=False, verbose_name="Descripcion")
    estado = models.IntegerField(null=False, blank=False, verbose_name="Estado")

    def __str__(self):
        return self.nombre_categoria



class Articulo(models.Model):
    nombre_articulo = models.CharField(max_length= 50, null=False,  blank=False, verbose_name="Nombre del articulo")
    precio_venta_articulo = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Precio venta")
    stock_articulo = models.IntegerField(null=False, blank=False, verbose_name="Stock")
    descripcion_articulo = models.CharField(max_length=255, null=False, blank=False, verbose_name="Descripcion del articuo")
    estado_articulo = models.IntegerField(null=False, blank=False, verbose_name="Estado")
    categoria_articulo = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_articulo

class Pesrsona(models.Model):
         
     
    Numero_documento = (
            ('C.C', 'Cedula de ciudanania'),
            ('C.E', 'Cedula de extranjería'),
            ('T.E', 'Tarjeta de extranjería ')
        )

    tipo_persona = models.CharField(max_length=20, null=False, blank=False, verbose_name="Tipo de persona")
    nombre  = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    tipo_documento = CharField(max_length=20, choices=Numero_documento, default='C.C')
    numero_documento = models.CharField(max_length=1, null=False, blank=False, verbose_name="Numero de documento" )
    direccion = models.CharField(max_length=70, null=False, blank=False, verbose_name="Direccion")
    telefono = models.CharField(max_length=20, verbose_name="Telefono")
    email = models.CharField(max_length=70, null=False, blank=False, verbose_name="Correo")

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=20)
    numero_documento = models.CharField(max_length=20)
    direccion = models.CharField(max_length=70)
    email = models.CharField(max_length=50)

class Venta(models.Model):
    tipo_comprobante = models.CharField(max_length=20,null=False, blank=False, verbose_name="Tipo de comprobante")
    serie_comprobante = models.CharField(max_length=7, null=False, blank=False, verbose_name="Serie del comprobante")
    numero_comprobante = models.CharField(max_length=10, null=False, blank=False, verbose_name="Numero de comprobante")
    fecha = models.DateTimeField(default=now,null=False, blank=False, verbose_name="Fecha")
    impuesto = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, verbose_name="Inpuesto")
    total = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, verbose_name="Total")
    estado = models.IntegerField(null=False, blank=False, verbose_name="Estado")
    id_cliente = models.ForeignKey(Pesrsona, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="id usuario")


class Detalle_venta(models.Model):
    detalle_venta = models.IntegerField(primary_key = True)     
    id_venta = models.IntegerField(null=False, blank=False, verbose_name="ID de la venta")  
    id_del_articulo = models.IntegerField(null=False, blank=False, verbose_name="ID de articulo")
    codigo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, blank=False)
    precio = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    impuesto  = models.DecimalField(default=0, max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Impuesto")
    descuanto  = models.DecimalField(default=0, max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Descuento")
    venta =  models.ForeignKey(Venta, on_delete=models.CASCADE)





class Ingreso(models.Model):
    id_proveedor = models.ForeignKey(Pesrsona, on_delete=models.CASCADE, verbose_name="id proveedor")
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="id usuario")
    tipo_comprobante = models.CharField(max_length=20, null=False, blank=False, verbose_name="Tipo de comprobante")
    serie_comprobante = models.CharField(max_length=7, null=False, blank=False)
    fecha = models.DateTimeField(default=now,null=False, blank=False, verbose_name="Fecha")
    impuesto = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, verbose_name="Inpuesto")
    total = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, verbose_name="Total")
    estado = models.IntegerField(null=False, blank=False, verbose_name="Estado")


class Detalle_ingreso(models.Model):
    id_detalle = models.IntegerField(primary_key = True, verbose_name="Id detalle")  
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name="id articulo")
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE, verbose_name="id ingreso")
    cantidad = models.IntegerField(null=False, blank=False, verbose_name="")
    precio =   models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, verbose_name="Precio")
    






from django.db import models
#from cities_light.abstract_models import AbstractCountry, AbstractRegion, AbstractCity
# Create your models here.

clasificacion = (
	(u'CONSTRUCCIÓN DE EDIFICACIONES',u'CONSTRUCCIÓN DE EDIFICACIONES'),
	(u'MANTENIMIENTO Y REMODELACIÓN DE EDIFICACIONES',u'MANTENIMIENTO Y REMODELACIÓN DE EDIFICACIONES'),
	(u'INFRAESTRUCTURA VIAL',u'INFRAESTRUCTURA VIAL'),
	(u'OBRAS DE URBANISMO O ESPACIO PUBLICO',u'OBRAS DE URBANISMO O ESPACIO PUBLICO'),
	(u'ADECUACION Y MOVIMIENTO DE TIERRAS',u'ADECUACION Y MOVIMIENTO DE TIERRAS'),
	(u'CONSULTORIA Y DISEÑO',u'CONSULTORIA Y DISEÑO'),
	(u'INTERVENTORIA EN INFRAESTRUCTURA VIAL',u'INTERVENTORIA EN INFRAESTRUCTURA VIAL'),
	(u'CONSTRUCCIÓN DE ALCANTARILLADOS Y ACUEDUCTOS',u'CONSTRUCCIÓN DE ALCANTARILLADOS Y ACUEDUCTOS'),
	(u'INFRAESTRUCTURA ELÉCTRICA',u'INFRAESTRUCTURA ELÉCTRICA'),
	(u'SUMINISTRO',u'SUMINISTRO'),
)

empresa = (
	(u'NDAM',u'NDAM'),
	(u'ARMELCO SAS',u'ARMELCO SAS'),
)


class Contrato(models.Model):
	numero 						= models.CharField(max_length=5,verbose_name=u'Número',blank=False, null=False)
	year						= models.IntegerField(verbose_name=u'Año',blank=False, null=False)
	numero_en_proponente		= models.IntegerField(verbose_name=u'Número en proponente',blank=False, null=False)
	objeto						= models.CharField(max_length=1000,verbose_name=u'Objeto',blank=False, null=False)
	tipo_de_obra				= models.CharField(max_length=1000,choices=clasificacion,verbose_name=u'Tipo de obra')
	entidad_contratante			= models.CharField(max_length=200,verbose_name=u'Entidad contratante',blank=False, null=False)
	valor_ejecutado				= models.DecimalField(max_digits=19, decimal_places=2,verbose_name=u'Valor ejecutado',blank=False, null=False)
	plazo_en_dias				= models.IntegerField(verbose_name=u'Plazo en días',blank=False, null=False)
	fecha_terminacion			= models.DateField(auto_now=False, auto_now_add=False,verbose_name=u'Fecha de terminación',blank=False, null=False)
	porcentaje_participacion 	= models.DecimalField(max_digits=6, decimal_places=5,verbose_name=u'Porcentaje de participación',blank=False, null=False)
	valor_en_sm					= models.DecimalField(max_digits=15, decimal_places=5,verbose_name=u'Valor en SM segun participación',blank=True, null=True)
	departamento				= models.CharField(max_length=200,verbose_name=u'Departamento',blank=False, null=False)
	municipio					= models.CharField(max_length=200,verbose_name=u'Municipio',blank=False, null=False)
	contrato					= models.FileField(upload_to='my_folder',blank=True, null=True)
	adicional1	 				= models.FileField(upload_to='my_folder',blank=True, null=True)
	adicional2 					= models.FileField(upload_to='my_folder',blank=True, null=True)
	acta_recibo_final			= models.FileField(upload_to='my_folder',blank=True, null=True)
	acta_liquidacion			= models.FileField(upload_to='my_folder',blank=True, null=True)
	certificacion_de_obra		= models.FileField(upload_to='my_folder',blank=True, null=True)
	certificacion_director		= models.FileField(upload_to='my_folder',blank=True, null=True)
	acuerdo_consorcial			= models.FileField(upload_to='my_folder',blank=True, null=True)
	empresa						= models.CharField(max_length=15,choices=empresa,verbose_name=u'empresa', default='NDAM')

	def get_absolute_url(self):
		return "/contrato/%i/" % self.id

	def __str__(self):
		return self.objeto




class ValorSM(models.Model):
	year	= models.IntegerField(verbose_name=u'Año')
	valor	= models.DecimalField(max_digits=15, decimal_places=5,verbose_name=u'Valor salario mínimo')
	def __str__(self):
		return str(self.valor)

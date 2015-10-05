from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class TimeStampModel(models.Model):

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Rubro(models.Model):
	id_rubro = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50, help_text='Nombre del rubro de la empresa')
	slug = models.SlugField(editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Rubro, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name=u'Categoria / Rubro'

class Empresa(TimeStampModel):
	id_empresa = models.AutoField(primary_key=True)
	logo = models.ImageField(upload_to='documents/%Y/%m/%d', null=True, blank=True, help_text='Imagen o Logo de la empresa')
	razonsocial = models.CharField(max_length = 140, help_text='Razon social de la empresa')
	slug = models.SlugField(editable = False)
	telefono = models.CharField(max_length = 50, help_text='Numero de telefono de la empresa')
	direccion = models.CharField(max_length = 140, help_text='Direccion de la empresa')
	latitud = models.CharField(max_length = 50,  null=True, blank=True, help_text='Latitud para la direccion en google maps')
	longitud = models.CharField(max_length = 50,  null=True, blank=True, help_text='Longitud para la direccion en google maps')
	rubro = models.ForeignKey(Rubro,db_column='id_rubro')

	user = models.ForeignKey(User)

	def save(self, *args, **kwargs):
		if not self.id_empresa:
			self.slug = slugify(self.razonsocial)
		super(Empresa, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.razonsocial

	class Meta:
		verbose_name=u'Empresa'
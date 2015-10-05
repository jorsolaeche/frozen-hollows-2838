from django.contrib import admin

from .models import Empresa, Rubro

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('razonsocial', 'created', 'modified', 'user',)
	fieldsets = (None, {'fields': ( ('razonsocial', 'logo'), 'rubro', ('telefono', 'direccion', 'latitud', 'longitud',), ('user',) ) }),
	list_filter = ['rubro',]
	search_fields = ('razonsocial',)

@admin.register(Rubro)
class RubroAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Empresa, Rubro

class RubroSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Rubro
		fields = ('id_rubro','nombre', 'slug')

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
	#rubros = RubroSerializer(many=True, read_only=True)
	rubro = RubroSerializer()
	class Meta:
		model = Empresa
		fields = ('id_empresa','logo', 'razonsocial', 'slug', 'direccion', 'latitud', 'longitud', 'telefono','rubro')
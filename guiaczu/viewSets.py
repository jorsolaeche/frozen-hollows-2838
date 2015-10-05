# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.filters import DjangoFilterBackend

from .models import Empresa, Rubro
from .serializers import EmpresaSerializer, RubroSerializer

class RubroViewSet(viewsets.ReadOnlyModelViewSet):

	model = Rubro
	queryset = Rubro.objects.all()
	serializer_class = RubroSerializer

class EmpresaViewSet(viewsets.ReadOnlyModelViewSet):

	model = Empresa
	queryset = Empresa.objects.all()
	serializer_class = EmpresaSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('id_empresa', 'rubro')
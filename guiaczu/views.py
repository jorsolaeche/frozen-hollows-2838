# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Empresa, Rubro

class RubroView(ListView):

	model = Rubro
	template_name = 'guiaczu/index.html'

class RubroDetailView(DetailView):

	model = Rubro
	context_object_name = 'rubro'

	def get_empresas(self, rubro):
		empresas = Empresa.objects.order_by('created').filter(rubro = rubro)
		return empresas

	def get_context_data(self, **kwargs):
		context = super(RubroDetailView, self).get_context_data(**kwargs)
		context['empresas'] = self.get_empresas(context['object'])
		return context

class EmpresaDetailView(DetailView):

	model = Empresa
	context_object_name = 'empresa'
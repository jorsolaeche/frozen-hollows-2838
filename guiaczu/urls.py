# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.decorators.cache import cache_page

from rest_framework import routers

from .views import RubroView, RubroDetailView, EmpresaDetailView
from .viewSets import EmpresaViewSet, RubroViewSet

router = routers.DefaultRouter()
router.register(r'rubros', RubroViewSet)
router.register(r'empresas', EmpresaViewSet)

urlpatterns = [
	#Index
	url(r'^$', RubroView.as_view()),
	#Rubro
	url(r'^rubro/(?P<slug>[-\w]+)/$' , RubroDetailView.as_view(), name = 'rubro_detail'),
	# Empresa
	url(r'^empresa/(?P<slug>[-\w]+)/$' , EmpresaDetailView.as_view(), name = 'empresa_detail'),
	url(r'^api/', include(router.urls)),
	
]
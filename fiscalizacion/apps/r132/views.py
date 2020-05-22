# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import TemplateView
from apps.r132.models import notif_notificacion, notif_pdo_localidad
from apps.r132.forms import NotificacionForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# from django.http import JsonResponse
# from django.shortcuts import render
# from apps.r132.serializers import PdoLocalidad_Serializers
# from apps.r132.pagination import StandardResultsSetPagination

# from apps.r132.serializers import PdoLocalidad_Serializers
# from django.shortcuts import get_object_or_404
# import json
# from django.core import serializers
# from rest_framework import generics
# from rest_framework.generics import ListAPIView





# def localidad(request):
#     lista = serializers.serialize('json', NotifPdoLocalidad.objects.all(), fields=['idstreet', 'partido', 'descripcion', 'ds_localidad', 'cp_postal'])
#     return HttpResponse(lista, content_type='application/json')


from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.r132 import serializers
# from apps.r132 import models

class PartidoViewset(viewsets.ModelViewSet):
	queryset = notif_pdo_localidad.objects.all()
	serializer_class = serializers.PdoLocalidad_Serializers
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('ds_localidad', 'cp_postal', 'partido', 'id','descripcion')

# class Home(TemplateView):
#     # template_name = 'bootstrap/home.html'
#     template_name = 'web.html'

# class Home(TemplateView):
#     # template_name = 'bootstrap/home.html'
#     template_name = 'blank.html'

class Home(TemplateView):
    # template_name = 'bootstrap/home.html'
    # template_name = 'web2.html'
    template_name = 'bootstrap/r132/home.html'

class Page1(TemplateView):
    # template_name = 'bootstrap/home.html'
    template_name = 'bootstrap/r132/page1.html'



class Inicio(TemplateView):
    # template_name = 'bootstrap/home.html'
    # template_name = 'materialize/index_materialize.html'
    template_name = 'bootstrap/r132/page1.html'

# class Inicio(TemplateView):
#     template_name = 'index.html'

class CargarR132(CreateView):
    model = notif_notificacion
    form_class = NotificacionForm
    # template_name = 'materialize/carga_inicial.html'
    template_name = 'bootstrap/r132/carga_inicial.html'
    success_url = reverse_lazy('r132:carga_inicial')
#     # success_url = reverse_lazy('informe:listar_informe_venta')

# #++++++++++++++++++++++++++++++++

# def pdoLocalidad(request):
# 	return render(request, "wine.html", {})

# class PdoLocalidadListar(ListAPIView):
#     # set the pagination and serializer class

# 	pagination_class = StandardResultsSetPagination
# 	serializer_class = PdoLocalidadSerializers

# 	def get_queryset(self):
#         # filter the queryset based on the filters applied

# 		queryList = NotifPdoLocalidad.objects.all()
# 		partido = self.request.query_params.get('partido', None)
# 		descripcion = self.request.query_params.get('descripcion', None)
# 		ds_localidad = self.request.query_params.get('ds_localidad', None)
# 		cp_postal = self.request.query_params.get('cp_postal', None)
# 		sort_by = self.request.query_params.get('sort_by', None)

# 		if partido:
# 		    queryList = queryList.filter(partido = partido)
# 		if descripcion:
# 		    queryList = queryList.filter(descripcion = descripcion)
# 		if ds_localidad:
# 		    queryList = queryList.filter(ds_localidad = ds_localidad)
# 		if cp_postal:
# 		    queryList = queryList.filter(cp_postal = cp_postal)    

#         # sort it if applied on based on partido/cp

# 		if sort_by == "partido":
# 		    queryList = queryList.order_by("partido")
# 		elif sort_by == "cp_postal":
# 		    queryList = queryList.order_by("cp_postal")
# 		return queryList


# def getPdo(request):
#     # get all the countreis from the database excluding 
#     # null and blank values

#     if request.method == "GET" and request.is_ajax():
#         partido = NotifPdoLocalidad.objects.exclude(partido__isnull=True).\
#             exclude(partido__exact='').order_by('partido').values_list('partido').distinct()
#         partido = [i[0] for i in list(partido)]
#         data = {
#             "partido": partido, 
#         }
#         return JsonResponse(data, status = 200)


# def getDescripcion(request):
#     if request.method == "GET" and request.is_ajax():
#         # get all the varities from the database excluding 
#         # null and blank values

#         descripcion = NotifPdoLocalidad.objects.exclude(descripcion__isnull=True).\
#         	exclude(descripcion__exact='').order_by('descripcion').values_list('descripcion').distinct()
#         descripcion = [i[0] for i in list(descripcion)]
#         data = {
#             "descripcion": descripcion, 
#         }
#         return JsonResponse(data, status = 200)


# def getLocalidad(request):
#     # get the provinces for given country from the 
#     # database excluding null and blank values

#     if request.method == "GET" and request.is_ajax():
#         cp_postal = request.GET.get('cp_postal')
#         ds_localidad = NotifPdoLocalidad.objects.filter(partido = partido).\
#             	exclude(ds_localidad__isnull=True).exclude(ds_localidad__exact='').\
#             	order_by('ds_localidad').values_list('ds_localidad').distinct()
#         ds_localidad = [i[0] for i in list(ds_localidad)]
#         data = {
#             "ds_localidad": ds_localidad, 
#         }
#         return JsonResponse(data, status = 200)


# def getCodigoPostal(request):
#     # get the regions for given province from the 
#     # database excluding null and blank values
    
#     if request.method == "GET" and request.is_ajax():
#         ds_localidad = request.GET.get('ds_localidad')
#         cp_postal = NotifPdoLocalidad.objects.filter(ds_localidad = ds_localidad).\
#                 exclude(cp_postal__isnull=True).exclude(cp_postal__exact='').values_list('cp_postal').distinct()
#         cp_postal = [i[0] for i in list(cp_postal)]
#         data = {
#             "cp_postal": cp_postal, 
#         }
#         return JsonResponse(data, status = 200)





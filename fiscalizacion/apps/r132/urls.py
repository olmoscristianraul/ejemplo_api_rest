from django.urls import path, include
# from django.conf import settings
# from django.contrib import admin
# from apps.r132.views import Inicio, CargarR132
from apps.r132.views import *

# from rest_framework.authtoken import views



urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('page1', Page1.as_view(), name = 'page1'),

	path('inicio/',Inicio.as_view(), name = 'inicio'),
	path('carga_inicial/',CargarR132.as_view(), name = 'carga_inicial'),
    
    # path('localidad/',Pdolocalidad.as_view(), name = 'localidad'),
    # path('localidad/',localidad, name = 'localidad'),



    # path('pdoLocalidad/',pdoLocalidad, name = 'pdoLocalidad'),

	# path("PdoLocalidadListar/", PdoLocalidadListar.as_view(), name = 'PdoLocalidadListar'),
 #    path("ajax/partido/", getPdo, name = 'get_partido'),
 #    path("ajax/descripcion/", getDescripcion, name = 'get_descripcion'),
 #    path("ajax/localidad/", getLocalidad, name = 'get_localidad'),
 #    path("ajax/cp/", getCodigoPostal, name = 'get_cp'),
]


# <script type="text/javascript">
# $(document).ready(function() {
#   $(function() {
#     $.ajax({
#       type: 'GET',
#       url: 'http://192.168.0.12:8000/api/unprefijo/',
#       format: 'json',
#       //dataType: 'application/json; charset=utf-8',
#       // Content-Type: 'application/json',

#       success: function(response) {
#         var resultado = response;
        
#         var datos = [];
#         for (var i = 0; i < resultado.length; i++) {
#           // datos[resultado[i].ds_localidad.trim()] = resultado[i].ds_localidad.trim()+','+resultado[i].partido+','+resultado[i].cp_postal+resultado[i].id

#           datos[resultado[i].id] = resultado[i].ds_localidad.trim()+','+resultado[i].partido+','+resultado[i].cp_postal+resultado[i].id

#           console.log(datos);
#           // console.log(datos[resultado[i].ds_localidad.trim()]);
#         }
#         $('input.autocomplete').autocomplete({
#             data: datos,
#             limit:10,
#             minLength:1,
#             onAutocomplete : function(seleccionado) {
#                 var datos = resultado[seleccionado.trim().toLowerCase().replace(" ","_")];
#                 // resultado[resultado[i].ds_localidad.trim().toLowerCase().replace(" ","_")] = resultado[i]
#                 console.log(datos);
#             },
#         });
#       }
#     });
#   });
# });
# </script>

from rest_framework import serializers
from apps.r132.models import notif_pdo_localidad
# from rest_framework.serializers import ModelSerializer



class PdoLocalidad_Serializers(serializers.ModelSerializer):
	class Meta:
	    model = notif_pdo_localidad
	    #fields = ("_all_")
	    #fields = ('idstreet', 'partido', 'descripcion', 'ds_localidad', 'cp_postal')
	    #fields = ('idstreet', 'partido', 'descripcion', 'ds_localidad', 'cp_postal')
	    #fields = ('ds_localidad',)
	    fields = ('ds_localidad', 'partido', 'cp_postal','id',)
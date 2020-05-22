# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
python manage.py inspectdb NotifAccion NotifAsignacion NotifEst
ado NotifForma NotifLoteOperativo NotifNotificacion NotifPdoLocalidad NotifRol N
otifSubAccion NotifTipoDomicilio NotifUsuario NotifUsuarioRol > apps\r132\models
.py
from django.db import models


class Notifaccion(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifAccion'


class Notifasignacion(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifAsignacion'


class Notifestado(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifEstado'


class Notifforma(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifForma'


class Notifloteoperativo(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifLoteOperativo'


class Notifnotificacion(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifNotificacion'


class Notifpdolocalidad(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifPdoLocalidad'


class Notifrol(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifRol'


class Notifsubaccion(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifSubAccion'


class Notiftipodomicilio(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifTipoDomicilio'


class Notifusuario(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifUsuario'


class Notifusuariorol(models.Model):

    class Meta:
        managed = False
        db_table = 'NotifUsuarioRol'

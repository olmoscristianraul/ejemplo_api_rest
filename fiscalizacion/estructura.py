# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class NotifAccion(models.Model):
    accion = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_accion'


class NotifAsignacion(models.Model):
    idnotificacion = models.ForeignKey('NotifNotificacion', models.DO_NOTHING, db_column='idnotificacion', blank=True, null=True)
    idusuario = models.ForeignKey('NotifUsuario', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)
    detalle = models.CharField(max_length=240, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_asignacion'


class NotifEstado(models.Model):
    estado = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_estado'


class NotifForma(models.Model):
    forma = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_forma'


class NotifLoteOperativo(models.Model):
    id = models.AutoField()
    num_lote = models.IntegerField()
    num_operativo = models.IntegerField(blank=True, null=True)
    cant_pdas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_lote_operativo'


class NotifNotificacion(models.Model):
    operativo = models.IntegerField(blank=True, null=True)
    idaccion = models.IntegerField(blank=True, null=True)
    idsubaccion = models.IntegerField(blank=True, null=True)
    partido = models.IntegerField()
    partida = models.IntegerField()
    expediente = models.CharField(max_length=20)
    contribuyente = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    id_tipo_domicilio = models.ForeignKey('NotifTipoDomicilio', models.DO_NOTHING, db_column='id_tipo_domicilio')
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    fecha_cargada = models.DateTimeField()
    idusuario_carga = models.IntegerField(blank=True, null=True)
    fecha_notificada = models.DateTimeField(blank=True, null=True)
    idusuario_notifica = models.IntegerField(blank=True, null=True)
    idestado = models.IntegerField(blank=True, null=True)
    idforma = models.IntegerField(blank=True, null=True)
    lote = models.IntegerField(blank=True, null=True)
    operativo_origen = models.IntegerField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    metros = models.FloatField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    cp = models.IntegerField(blank=True, null=True)
    pdo_notif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_notificacion'


class NotifPdoLocalidad(models.Model):
    idstreet = models.IntegerField(blank=True, null=True)
    partido = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    ds_localidad = models.CharField(max_length=100, blank=True, null=True)
    cp_postal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_pdo_localidad'


class NotifRol(models.Model):
    rol = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_rol'


class NotifSubAccion(models.Model):
    sub_accion = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_sub_accion'


class NotifTipoDomicilio(models.Model):
    tipo_domicilio = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_tipo_domicilio'


class NotifUsuario(models.Model):
    usuario = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'notif_usuario'


class NotifUsuarioRol(models.Model):
    idusuario = models.ForeignKey(NotifUsuario, models.DO_NOTHING, db_column='idusuario', blank=True, null=True)
    idrol = models.ForeignKey(NotifRol, models.DO_NOTHING, db_column='idrol', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notif_usuario_rol'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class notif_accion(models.Model):
    accion = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notif_accion'

    def __str__(self):
        return '{}'.format(str(self.accion))

class notif_usuario(models.Model):
    usuario = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'notif_usuario'

class notif_tipo_domicilio(models.Model):
    tipo_domicilio = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notif_tipo_domicilio'

    def __str__(self):
        return '{}'.format(str(self.tipo_domicilio))


class notif_sub_accion(models.Model):
    sub_accion = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notif_sub_accion'

    def __str__(self):
        return '{}'.format(str(self.sub_accion))

class notif_lote_operativo(models.Model):
    num_lote = models.IntegerField()
    num_operativo = models.IntegerField(blank=True, null=True)
    cant_pdas = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'notif_lote_operativo'

    def __str__(self):
        return '{}'.format(str(self.num_lote))


class notif_estado(models.Model):
    estado = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notif_estado'

    def __str__(self):
        return '{}'.format(str(self.estado))


class notif_forma(models.Model):
    forma = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notif_forma'

    def __str__(self):
        return '{}'.format(str(self.forma))



class notif_pdo_localidad(models.Model):
    idstreet = models.IntegerField(blank=True, null=True)
    partido = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    ds_localidad = models.CharField(max_length=100, blank=True, null=True)
    cp_postal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notif_pdo_localidad'

    def __str__(self):
        # return '{}'.format(str(self.partido)+'-'+str(self.descripcion)+'-'+str(self.ds_localidad)+'-'+str(self.cp_postal))
        return '{}'.format(str(self.ds_localidad))


class notif_rol(models.Model):
    rol = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notif_rol'
        

class notif_usuario_rol(models.Model):
    idusuario = models.ForeignKey(notif_usuario, blank=True, null=True, on_delete=models.CASCADE)
    idrol = models.ForeignKey(notif_rol, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'notif_usuario_rol'


class notif_notificacion(models.Model):
    operativo = models.IntegerField(blank=True, null=True)
    idaccion = models.ForeignKey(notif_accion, null=True, blank=True, on_delete=models.CASCADE)
    idsubaccion = models.ForeignKey(notif_sub_accion, null=True, blank=True, on_delete=models.CASCADE)
    partido = models.IntegerField()
    partida = models.IntegerField()
    expediente_organismo = models.IntegerField()
    expediente_numero = models.CharField(max_length=7)
    expediente_ceros = models.CharField(max_length=4)
    expediente_alcance = models.CharField(max_length=20)
    expediente = models.CharField(max_length=20)
    contribuyente = models.CharField(max_length=100)
    localidad = models.ForeignKey(notif_pdo_localidad, null=True, blank=True, on_delete=models.CASCADE)
    id_tipo_domicilio = models.ForeignKey(notif_tipo_domicilio, null=True, blank=True, on_delete=models.CASCADE)
    # id_tipo_domicilio = models.ForeignKey('NotifTipoDomicilio', models.DO_NOTHING, db_column='id_tipo_domicilio')
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    fecha_cargada = models.DateTimeField()
    idusuario_carga = models.IntegerField(blank=True, null=True)
    fecha_notificada = models.DateTimeField(blank=True, null=True)
    idusuario_notifica = models.IntegerField(blank=True, null=True)
    idestado = models.ForeignKey(notif_estado, null=True, blank=True, on_delete=models.CASCADE)
    idforma = models.ForeignKey(notif_forma, null=True, blank=True, on_delete=models.CASCADE)
    lote = models.IntegerField(blank=True, null=True)
    operativo_origen = models.IntegerField(blank=True, null=True)
    fecha_salida = models.DateTimeField(verbose_name=('Fecha Salida'), null=True, blank=True)
    metros = models.FloatField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    cp = models.IntegerField(null=True, blank=True)
    pdo_notif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notif_notificacion'

    def __str__(self):
        return '{}'.format(str(self.id))


class notif_asignacion(models.Model):
    # idnotificacion = models.ForeignKey(notif_notificacion, blank=True, null=True)
    idnotificacion = models.ForeignKey(notif_notificacion, null=True, blank=True, on_delete=models.CASCADE)
    idusuario = models.ForeignKey(notif_usuario, blank=True, null=True, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=240, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notif_asignacion'


# class Sysdiagrams(models.Model):
#     name = models.CharField(max_length=128)
#     principal_id = models.IntegerField()
#     diagram_id = models.AutoField(primary_key=True)
#     version = models.IntegerField(blank=True, null=True)
#     definition = models.BinaryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sysdiagrams'
#         unique_together = (('principal_id', 'name'),)

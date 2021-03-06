# Generated by Django 2.2 on 2020-02-17 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notif_accion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'notif_accion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'notif_estado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_forma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'notif_forma',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_lote_operativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_lote', models.IntegerField()),
                ('num_operativo', models.IntegerField(blank=True, null=True)),
                ('cant_pdas', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='notif_pdo_localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idstreet', models.IntegerField(blank=True, null=True)),
                ('partido', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('ds_localidad', models.CharField(blank=True, max_length=100, null=True)),
                ('cp_postal', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'notif_pdo_localidad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=10)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'notif_rol',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_sub_accion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_accion', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'notif_sub_accion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_tipo_domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_domicilio', models.CharField(max_length=20)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'notif_tipo_domicilio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'notif_usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_usuario_rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idrol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_rol')),
                ('idusuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_usuario')),
            ],
            options={
                'db_table': 'notif_usuario_rol',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operativo', models.IntegerField(blank=True, null=True)),
                ('partido', models.IntegerField()),
                ('partida', models.IntegerField()),
                ('expediente_organismo', models.IntegerField()),
                ('expediente_numero', models.CharField(max_length=7)),
                ('expediente_ceros', models.CharField(max_length=4)),
                ('expediente_alcance', models.CharField(max_length=20)),
                ('expediente', models.CharField(max_length=20)),
                ('contribuyente', models.CharField(max_length=100)),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('fecha_cargada', models.DateTimeField()),
                ('idusuario_carga', models.IntegerField(blank=True, null=True)),
                ('fecha_notificada', models.DateTimeField(blank=True, null=True)),
                ('idusuario_notifica', models.IntegerField(blank=True, null=True)),
                ('lote', models.IntegerField(blank=True, null=True)),
                ('operativo_origen', models.IntegerField(blank=True, null=True)),
                ('fecha_salida', models.DateTimeField(blank=True, null=True, verbose_name='Fecha Salida')),
                ('metros', models.FloatField(blank=True, null=True)),
                ('monto', models.FloatField(blank=True, null=True)),
                ('cp', models.IntegerField(blank=True, null=True)),
                ('pdo_notif', models.IntegerField(blank=True, null=True)),
                ('id_tipo_domicilio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_tipo_domicilio')),
                ('idaccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_accion')),
                ('idestado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_estado')),
                ('idforma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_forma')),
                ('idsubaccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_sub_accion')),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_pdo_localidad')),
            ],
            options={
                'db_table': 'notif_notificacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='notif_asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(blank=True, max_length=240, null=True)),
                ('idnotificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_notificacion')),
                ('idusuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='r132.notif_usuario')),
            ],
            options={
                'db_table': 'notif_asignacion',
                'managed': True,
            },
        ),
    ]

from django.contrib import admin
from apps.r132.models import notif_accion, notif_usuario, notif_tipo_domicilio, notif_sub_accion, notif_notificacion, \
notif_asignacion, notif_estado, notif_lote_operativo, notif_forma, notif_pdo_localidad, notif_rol, notif_usuario_rol

admin.site.register(notif_accion)
admin.site.register(notif_usuario)
admin.site.register(notif_tipo_domicilio)
admin.site.register(notif_sub_accion)
admin.site.register(notif_lote_operativo)
admin.site.register(notif_notificacion)
admin.site.register(notif_asignacion)
admin.site.register(notif_estado)
admin.site.register(notif_forma)
admin.site.register(notif_pdo_localidad)
admin.site.register(notif_rol)
admin.site.register(notif_usuario_rol)

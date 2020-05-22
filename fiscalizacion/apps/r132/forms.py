# -*- coding: utf-8 -*-

from django import forms

from apps.r132.models import notif_notificacion

#from bootstrap_datepicker_plus import DateTimePickerInput
#from bootstrap_datepicker.widgets import DatePicker



# class NotificacionForm(forms.ModelForm):
    
#     class Meta:
#         model = NotifNotificacion
#         fields = ['partido','fecha_salida']

#     date = forms.DateTimeField(
#         input_formats=['%d/%m/%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     ),

#     partido =  forms.TextInput(
#         attrs={
#             'required': True,
#             'class': 'form-control',
#             'placeholder': 'Partido',
#             'id': 'partido'
#         }
#     )

# widgets = {
#             'name': Textarea(attrs={'cols': 80, 'rows': 20}),
#         }


class NotificacionForm(forms.ModelForm):

    class Meta:
        model = notif_notificacion
        fields = ['operativo','idaccion','idsubaccion','partido','partida','expediente','contribuyente','localidad','id_tipo_domicilio','calle','numero','fecha_cargada','idusuario_carga','fecha_notificada','idusuario_notifica','idestado','idforma','lote','operativo_origen','fecha_salida','metros','monto','cp','pdo_notif',]
        labels = {
        'operativo':'operativo',
        'idaccion':'idaccion',
        'idsubaccion':'idsubaccion',
        'partido':'partido',
        'partida':'partida',
        'expediente':'expediente',
        'contribuyente':'contribuyente',
        'localidad':'localidad',
        'id_tipo_domicilio':'id_tipo_domicilio',
        'calle':'calle',
        'numero':'numero',
        'fecha_cargada':'fecha_cargada',
        'idusuario_carga':'idusuario_carga',
        'fecha_notificada':'fecha_notificada',
        'idusuario_notifica':'idusuario_notifica',
        'idestado':'idestado',
        'idforma':'idforma',
        'lote':'lote',
        'operativo_origen':'operativo_origen',
        # 'fecha_salida':'fecha_salida',
        'metros':'metros',
        'monto':'monto',
        'cp':'cp',
        'pdo_notif':'pdo_notif',
        }

        widgets = {
            # 'fecha_salida': 
            'fecha_salida':forms.DateInput(attrs={'class':'form-control', 
                               'placeholder':'Fecha Salida',
                               'type': 'Date'}),
        
            'partido': forms.TextInput(
                attrs={
                    'required': True,
                    'class': 'form-control',
                    'placeholder': 'Partido',
                    'id': 'partido'
                }
            ),

            'partida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Partida',
                    'id': 'partida'
                }
            ),

            'idaccion': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control',
                    'placeholder': 'Acción',
                    'id': 'idaccion'
                }
            ),

            'idsubaccion': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control',
                    'placeholder': 'Sub-accion',
                    'id': 'idsubaccion'
                }
            ),

            'operativo_origen': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Op. Origen',
                    'id': 'operativo_origen'
                }
            ),

            'metros': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Metros',
                    'id': 'metros'
                }
            ),

            'monto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Monto',
                    'id': 'monto'
                }
            ),

            'id_tipo_domicilio': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control',
                    'placeholder': 'Domicilio Tipo',
                    'id': 'id_tipo_domicilio'
                }
            ),

            'calle': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Calle',
                    'id': 'calle'
                }
            ),

            'numero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número',
                    'id': 'numero'
                }
            ),

            'localidad': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control',
                    'placeholder': 'Localidad',
                    'id': 'localidad'
                }
            ),

            'pdo_notif': forms.TextInput(
                attrs={
                    'required': True,
                    'class': 'form-control',
                    'placeholder': 'Pdo. ',
                    'id': 'pdo_notif'
                }
            ),

            'cp': forms.TextInput(
                attrs={
                    'required': True,
                    'class': 'form-control',
                    'placeholder': 'CP',
                    'id': 'cp'
                }
            ),
        }
from django.urls import path, include
# from django.conf import settings
from django.contrib import admin

# from rest_framework.authtoken import views
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('r132/', include(('apps.r132.urls', 'r132'))),

    path('api/', include(router.urls)),
]


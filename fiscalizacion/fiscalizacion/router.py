from apps.r132.views import PartidoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('unprefijo', PartidoViewset)
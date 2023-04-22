from rest_framework import routers
from .api import CocinaViewSet

router = routers.DefaultRouter()

router.register('api/recetas', CocinaViewSet, 'Recetas')

urlpatterns = router.urls 
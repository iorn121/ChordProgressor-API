from rest_framework import routers
from chord.views import ChordViewSet

router=routers.DefaultRouter()
router.register('chord',ChordViewSet)
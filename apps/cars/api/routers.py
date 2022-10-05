from rest_framework.routers import DefaultRouter
from apps.cars.api.views import CarViewSet,CategoryViewSet, DescriptionViewSet


router= DefaultRouter()

router.register(prefix='categories', basename='categories', viewset=CategoryViewSet)
router.register(prefix='descriptions', basename='descriptions', viewset=DescriptionViewSet)
router.register(prefix='cars', basename='cars', viewset=CarViewSet)

urlpatterns = router.urls 

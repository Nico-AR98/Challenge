from rest_framework.viewsets import ModelViewSet

from apps.cars.models import Car,Category,Description
from apps.cars.api.serializers import CarSerializer,DescriptionSerializer,CategorySerializer

class CategoryViewSet(ModelViewSet):
    serializer_class =CategorySerializer
    queryset=Category.objects.all()

class DescriptionViewSet(ModelViewSet):
    serializer_class =DescriptionSerializer
    queryset=Description.objects.all()


class CarViewSet(ModelViewSet):
    serializer_class =CarSerializer
    queryset=Car.objects.all()


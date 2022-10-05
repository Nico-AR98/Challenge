from rest_framework.serializers import ModelSerializer

from apps.cars.models import Car, Category,Description


class DescriptionSerializer(ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'

class CarSerializer(ModelSerializer):

    detail= DescriptionSerializer(many=True, read_only=True, source = 'description_set')
    class Meta:
        model = Car
        fields = ('id','brand','model','miniature_img','price','release_year','category','detail')

        

class CategorySerializer(ModelSerializer):
    cars= CarSerializer(many=True, read_only=True, source = 'car_set')
    class Meta:
        model = Category
        fields = ('name','cars')



    

        


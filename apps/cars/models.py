from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):

    brand = models.CharField(max_length=50)

    model = models.CharField(max_length=50)

    miniature_img = models.ImageField(upload_to ='cars/')

    price = models.PositiveIntegerField()

    release_year= models.PositiveSmallIntegerField()

    category = models.ForeignKey(Category,null=False,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        txt = '{0} - {1}'
        return txt.format(self.model,self.release_year)

class Description(models.Model):

    car_id = models.ForeignKey(Car,null=False,blank=False,on_delete=models.CASCADE)

    illustrative_img = models.ImageField(upload_to ='cars/')

    title = models.CharField(max_length=50)

    body =models.TextField()

    types = [
        ('Top','Top'),
        ('Card','Card'),
        ('Low','Lower'),
    ]

    type = models.CharField(max_length=4,choices= types,default='Top')

    def __str__(self):
        txt = '{0} - {1}'
        return txt.format(self.car_id,self.type)

    

    

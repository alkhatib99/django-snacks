from django.db import models

# Create your models here.


class ColdDrink(models.Model):
    name = models.CharField(max_length=255)
    size=models.FloatField()
    price=models.IntegerField()


    def __str__(self) :
        return self.name

class HotDrink(models.Model):
    name = models.CharField(max_length=255)
    size=models.FloatField()
    price=models.IntegerField()

    def __str__(self) :
        return self.name



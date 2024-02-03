from django.db import models
from django.contrib.postgres.fields import ArrayField

class Category(models.Model):
    name = models.CharField(max_length=127)
    image = models.FileField(upload_to='category_images')
    slug = models.CharField(max_length=127, unique=True)
    description = models.TextField()
    father_category = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    fields = ArrayField(models.CharField(max_length=127), default=list)
    def __str__(self) -> str:
        return self.name
    
# PC stuff models
class PCStuffSize(models.Model):
    value = models.CharField(max_length=127)
    
    def __str__(self) -> str:
        return self.value
    
class PCStuffFrequency(models.Model):
    value = models.FloatField()
    
    def __str__(self) -> str:
        return str(self.value)
    
class PCStuffBrand(models.Model):
    value = models.CharField(max_length=127)
    
    def __str__(self) -> str:
        return self.value

# Home staff models
class HomeStaffRooms(models.Model):
    value = models.IntegerField()
    
    def __str__(self) -> str:
        return str(self.value)

class HomeStaffMaterial(models.Model):
    value = models.CharField(max_length=127)
    
    def __str__(self) -> str:
        return self.value

class HomeStaffBrand(models.Model): 
    value = models.CharField(max_length=127)     
    
    def __str__(self) -> str:
        return self.value

class Item(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    image = models.FileField(upload_to='item_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # fields for category Monitors 
    size = models.ForeignKey(PCStuffSize, null=True, blank=True, on_delete=models.CASCADE)
    
    #fields for category PC parts
    frequency = models.ForeignKey(PCStuffFrequency, null=True, blank=True, on_delete=models.CASCADE)

    #fields for category PC stuff 
    brand = models.ForeignKey(PCStuffBrand, null=True, blank=True, on_delete=models.CASCADE)

    # fields for category House 
    rooms = models.ForeignKey(HomeStaffRooms, null=True, blank=True, on_delete=models.CASCADE)
    
    #fields for category Home parts
    material = models.ForeignKey(HomeStaffMaterial, null=True, blank=True, on_delete=models.CASCADE)

    #fields for category Home staff 
    brand_house = models.ForeignKey(HomeStaffBrand, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
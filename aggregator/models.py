from django.db import models
from django.contrib.auth.models import User
from aggregator.categories import CATEGORIES, SUBCATEGORIES

# Create your models here.
class UserProfile(models.Model):
    # All commented fields are already in Default Django User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)    
    #username = models.CharField(max_length=30)
    #password = models.CharField(max_length=32)
    #email = models.CharField(max_length=50)    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Category(models.Model):
    name = models.CharField(max_length=31, choices=CATEGORIES)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, choices=SUBCATEGORIES)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.name}, {self.description}, {self.price}'


class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')

    def __str__(self):
        return f'{self.post}, {self.file_name}, {self.photo}'



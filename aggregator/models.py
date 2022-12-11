from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(Category, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=12, decimal_places=2)

class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo')


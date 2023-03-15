from django.db import models


# Create your models here.

class Product(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='products')
  
  def __str__(self):
    return self.name


class Cart(models.Model):
  items = models.ManyToManyField(Product)
  total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  date_added = models.DateTimeField(auto_now_add=True)

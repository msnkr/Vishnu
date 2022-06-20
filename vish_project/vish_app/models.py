from django.db import models

# Create your models here.
class Products(models.Model):
    product_title = models.CharField(max_length=50)
    product_description = models.TextField()
    product_price = models.CharField(max_length=10)
    product_image = models.ImageField()

    def __str__(self):
        return self.product_title


class ContactPage(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    number = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name
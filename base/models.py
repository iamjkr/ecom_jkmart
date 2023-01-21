from django.db import models

# Create your models here

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('CR', 'Curd'),
        ('ML', 'Milk'),
        ('LS', 'Lassi'),
        ('MS', 'Milkshake'),
        ('PN', 'Paneer'),
        ('GH', 'Ghee'),
        ('IC', 'Ice Cream'),

    )

    title = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    composition = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2,default='ML')
    image = models.ImageField(upload_to='media/product_images/')


    def __str__(self):
        return self.title

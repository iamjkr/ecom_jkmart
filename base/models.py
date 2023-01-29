from django.contrib.auth.models import User
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
        ('CH', 'Cheese'),

    )

    title = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    composition = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='ML')
    image = models.ImageField(upload_to='media/product_images/')

    def __str__(self):
        return self.title


class Customer(models.Model):
    ANDHRA_PRADESH = 'AP'
    ARUNACHAL_PRADESH = 'AR'
    ASSAM = 'AS'
    BIHAR = 'BR'
    CHHATTISGARH = 'CT'
    GOA = 'GA'
    GUJARAT = 'GJ'
    HARYANA = 'HR'
    HIMACHAL_PRADESH = 'HP'
    JHARKHAND = 'JH'
    KARNATAKA = 'KA'
    KERALA = 'KL'
    MADHYA_PRADESH = 'MP'
    MAHARASHTRA = 'MH'
    MANIPUR = 'MN'
    MEGHALAYA = 'ML'
    MIZORAM = 'MZ'
    NAGALAND = 'NL'
    ODISHA = 'OD'
    PUNJAB = 'PB'
    RAJASTHAN = 'RJ'
    SIKKIM = 'SK'
    TAMIL_NADU = 'TN'
    TELANGANA = 'TG'
    TRIPURA = 'TR'
    UTTAR_PRADESH = 'UP'
    UTTARAKHAND = 'UK'
    WEST_BENGAL = 'WB'
    STATE_CHOICES = [
        (ANDHRA_PRADESH, 'Andhra Pradesh'),
        (ARUNACHAL_PRADESH, 'Arunachal Pradesh'),
        (ASSAM, 'Assam'),
        (BIHAR, 'Bihar'),
        (CHHATTISGARH, 'Chhattisgarh'),
        (GOA, 'Goa'),
        (GUJARAT, 'Gujarat'),
        (HARYANA, 'Haryana'),
        (HIMACHAL_PRADESH, 'Himachal Pradesh'),
        (JHARKHAND, 'Jharkhand'),
        (KARNATAKA, 'Karnataka'),
        (KERALA, 'Kerala'),
        (MADHYA_PRADESH, 'Madhya Pradesh'),
        (MAHARASHTRA, 'Maharashtra'),
        (MANIPUR, 'Manipur'),
        (MEGHALAYA, 'Meghalaya'),
        (MIZORAM, 'Mizoram'),
        (NAGALAND, 'Nagaland'),
        (ODISHA, 'Odisha'),
        (PUNJAB, 'Punjab'),
        (RAJASTHAN, 'Rajasthan'),
        (SIKKIM, 'Sikkim'),
        (TAMIL_NADU, 'Tamil Nadu'),
        (TELANGANA, 'Telangana'),
        (TRIPURA, 'Tripura'),
        (UTTAR_PRADESH, 'Uttar Pradesh'),
        (UTTARAKHAND, 'Uttarakhand'),
        (WEST_BENGAL, 'West Bengal'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name

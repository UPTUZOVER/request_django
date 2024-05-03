from django.db import models
from django.utils import timezone
import uuid
from ckeditor.fields import RichTextField
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


class Categories(models.Model):

    name = models.CharField(max_length=50)

    class Meta:

        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = ("Brand")
        verbose_name_plural = ("Brands")

    def __str__(self):
        return self.name


class Color(models.Model):

    name = models.CharField(max_length=784)
    code = models.CharField(max_length=99)
    
    class Meta:
        verbose_name = ("Color")
        verbose_name_plural = ("Colors")

    def __str__(self):
        return self.name


class Filter_Price(models.Model):
    FILTER_PRICE= (
        ('100 TO 1000','100 TO 1000'),
        ('1000 TO 2000','1000 TO 2000'),
        ('2000 TO 3000','2000 TO 3000'),
        ('3000 TO 4000','3000 TO 4000'),
        ('4000 TO 5000','4000 TO 5000'),
        ('5000 TO 10000','5000 TO 10000'),
        ('10000 TO infinite','10000 TO infinite'),
    )
    
    price = models.CharField(choices=FILTER_PRICE, max_length=680)

    class Meta:
        verbose_name = ("Filter_Price")
        verbose_name_plural = ("Filter_Prices")

    def __str__(self):
        return self.price
    

class Product(models.Model):

    CONDITION = (('New', 'New'),('Old', 'Old'))
    STOCK = ('IN STOCK', 'IN STOCK'), ('OUT OF STOCK', 'OUT OF STOCK')
    STATUS = ('PUBLISH', 'PUBLIC'), ('DRAFT', 'DRAFT')

    unique_id = models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4())
    image = models.ImageField(upload_to='Product_images/img')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION, max_length=100)
    information = RichTextField(null=True)
    description = RichTextField(null=True)
    stock = models.CharField(choices=STOCK, max_length=200) 
    status = models.CharField(choices=STATUS, max_length=200)
    created_data = models.DateTimeField(default=timezone.now, max_length=545)
    
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_data and self.id:
            self.unique_id = self.created_data.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)
        
        
    
    class Meta:
        verbose_name = ("Products")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name


class Images(models.Model):

    image = models.ImageField(upload_to='Product_images/img')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Image")
        verbose_name_plural = ("Images")


class Tag(models.Model):

    name = models.CharField(max_length=300)
    product = models.ForeignKey(Product, related_name="imagess", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.name


class Contact_us(models.Model):

    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Contact_us")
        verbose_name_plural = ("Contact_uss")

    def __str__(self):
        return self.email















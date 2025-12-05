from unicodedata import category
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/', null=True, blank=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    stars = models.IntegerField(default=3)
    description = models.TextField()
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.destination.name}"


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=200)  
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Confirmed', 'Confirmed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"Booking {self.id} - {self.customer.name}"
    
class Product(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=200, null=True)
    productDescript =  RichTextUploadingField(null=True)
    weight = models.CharField(max_length=200, null=True)
    availability = models.CharField(max_length=200, null=True)
    shipping = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to='images/Products/',null=True,blank=True)
    productDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):         
        return self.productName
    
class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=True)
    categoryImage = models.ImageField(upload_to='images/Categories/',null=True,blank=True)
    def __str__(self):         
        return self.categoryName
    
class ProductDetail(models.Model):
    productDetailName = models.CharField(max_length=200, null=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    Description =  RichTextUploadingField(null=True)
    Information = RichTextUploadingField(null=True)
    Reviews = RichTextUploadingField(null=True)
    productDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    def __str__(self):         
        return f'{self.id} - {self.productDetailName} - {self.productID.productName}'
    
class ProductDetailImage(models.Model):
    productDetailImageName = models.CharField(max_length=200, null=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    productDetailImage = models.ImageField(upload_to='images/productDetail/',null=True,blank=True)
    imageDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):         
        return  f'{self.id} - {self.productDetailName} - {self.productID.productName}'

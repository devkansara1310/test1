from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    cno = models.CharField(max_length=15)
    pincode = models.IntegerField(max_length=6)

    def __str__(self):
        return self.first_name + self.last_name

class Product(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    qty = models.IntegerField(max_length=10)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_id) + ' | ' + str(self.product_id)

    @property
    def get_total(self):
        total = self.unit_price * self.qty
        return total
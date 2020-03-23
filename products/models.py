from django.db import models

# Create your models here.

class Product(models.Model):
    """This model is used for Product details"""
    name = models.CharField(max_length=50,null=True,blank=True)
    code = models.CharField(max_length=20,null=True,blank=True)
    # price = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    active = models.BooleanField(default=1,null=True,blank=True)
    detail = models.TextField(max_length=300,null=True,blank=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class Cart(models.Model):
    """This models is used for add product to card"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)


    class Meta:
        db_table = 'cart'

    def __str__(self):
        return self.product

    def get_price(self, obj):
        return obj.get_price

class CartItem(models.Model):
    """This models is used for Cart Item"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'cartitem'

    def __str__(self):
        return self.cart


class Coupon(models.Model):
    """This models is used for Coupon"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_value = models.PositiveIntegerField()

    class Meta:
        db_table = 'coupon'
        def __str__(self):
            return self.product


class OrderProduct(models.Model):
    """This model is used for create an order from a cart"""
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    oerder_plcae = models.BooleanField(default=False)

    class Meta:
        db_table = 'orderproduct'

    # def __str__(self):
    #     return str(self.cart_id)

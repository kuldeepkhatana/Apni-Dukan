from django.contrib import admin
from products.models import *
# Register your models here.



admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Coupon)
admin.site.register(OrderProduct)
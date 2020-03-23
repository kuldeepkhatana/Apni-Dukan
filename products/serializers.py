from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderProductSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    oerder_plcae = serializers.BooleanField(write_only=True)
    class Meta:

        model = OrderProduct
        fields = ('id','oerder_plcae','cart')



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'



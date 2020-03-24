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
    cart = CartSerializer(many=True)
    oerder_plcae = serializers.BooleanField(write_only=True)
    class Meta:

        model = OrderProduct
        fields = ('id','oerder_plcae','cart')

        def create(self, validated_data):
            cart_data = validated_data.pop('cart')
            order_data = OrderProduct.objects.create(**validated_data)

            for cart in cart_data:
                cart, created = Cart.objects.get_or_create(name=cart['name'])
                order_data.cart.add(cart)
            return order_data



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'



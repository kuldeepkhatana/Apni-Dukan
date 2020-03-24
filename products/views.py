from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework import viewsets, mixins, status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class AddCart(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer





class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# class AddOrderProduct(generics.CreateAPIView):
#     queryset = OrderProduct.objects.all()
#     serializer_class = OrderProductSerializer


# class AddOrderProductDetail(generics.CreateAPIView):
#     queryset = OrderProduct.objects.all()
#     serializer_class = OrderProductSerializer


class AddCartApiView(APIView):
    """API to save User Log Activity.

    """
    # permission_classes = (AllowAny,)
    # rendered_classes = (JSONRenderer,)


    def post(request):
        data = request.data

        try:
            if 'cart' in data and data['cart'] != '':
                cart = data['cart']
            else:
                return Response('Product missing', "", status=403)

            # if 'order_place' in data and data['order_place'] == True:
            #     if 'cart' in data and data['cart'] != '':
            #         cart = data['cart']
            #     else:
            #         return Response(response.parsejson('cart is missing', "", status=403))

                
            activity_data = OrderProduct.objects.filter(cart=cart).first()

            if activity_data is None:
                temp_data = OrderProduct()
                temp_data.order_place = order_place
                temp_data.cart_id = cart.object.first()
                temp_data.save()
            
            return Response("Success", status=201)

        except Exception as exp:
            return Response(exp, status=403)


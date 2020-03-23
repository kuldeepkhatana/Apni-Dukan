from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework import viewsets, mixins, status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class AddCart(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer





class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class AddOrderProduct(generics.CreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class AddOrderProductDetail(generics.CreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class SaveOderProductApiView(APIView):
    """
    API to save listings count View.
    """
    permission_classes = (AllowAny,)
    rendered_classes = (JSONRenderer,)

    def post(self, request):
        """
        API to Place Order.
        :param 1: cart_id
        :param 2: Boolean Field
        :return: Order Place Succesfully.
        """
        try:
            data = request.data
            count = 0

            if 'cart' in data and data['cart'] != '':
                cart = data['cart']
            else:
                return Response({'msg': 'Cart id is required', 'status': 422})


            try:
                listing_data_log = OrderProduct.objects.filter(cart_id=cart).first()
                if listing_data_log is None:
                    listing_data_log = OrderProduct()
                    listing_data_log.cart_id = cart
                    listing_data_log.oerder_plcae = oerder_plcae
                    listing_data_log.save()
                return Response({'msg':'Success', 'status': 200})
            except Exception as error:
                return Response({"msg": 'Please provide all details', 'status': 422})







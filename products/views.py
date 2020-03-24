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


class AddOrderProduct(generics.CreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class AddOrderProductDetail(generics.CreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer





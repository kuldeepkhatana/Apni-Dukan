from django.urls import path
from .views import *
urlpatterns = [
    path('add-cart/',AddCart.as_view()),
    path('add-cart/<int:pk>/',CartDetail.as_view()),
    path('add-order/', AddCartApiView.as_view()),
    # path('add-order/<int:pk>/',AddOrderProductDetail.as_view()),


]
